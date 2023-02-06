from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from users.seralizers import *
from users.models import *
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework.generics import CreateAPIView

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.
class Register_User(APIView):

    def post(self,request):
        data = request.data
        password=data['password']
        confirm_password=data['confirm_password']


        if password==confirm_password:
            rs=RegisterSerializer(data=data)
            if rs.is_valid():

                rs.save()
                content={'Message':"User created successfully"}
            return Response(content,status=status.HTTP_201_CREATED)

        else:
            content={'message':"Password and confirm password are not equal"}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)


class User_Login(APIView):
    def post(self,request):
        data=request.data
        username=data['username']
        password=data['password']

        try:
            rs=Register.objects.get(username=username,password=password)
            #payobj={'usename':rs.username,'password':rs.password,'email':rs.email,'created_at':str(rs.created_at),'updated_at':str(rs.updated_at)}
            payload = jwt_payload_handler(rs)
            token=jwt_encode_handler(payload)
            content={'message':'User Logged in successfully','token':token}
            return Response(content,status=status.HTTP_200_OK)


        except Register.DoesNotExist:
            content={'message':"Invalid Username and Password"}
            return Response(content,status=status.HTTP_404_NOT_FOUND)


class Create_Movie(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]


    def post(self,request):
        print(request.user)
        data=request.data

        ms=MovieSerializer(data=data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data,status=status.HTTP_200_OK)
        else:
            return Response(ms.errors,status=status.HTTP_400_BAD_REQUEST)


class Cast_Movie(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data=request.data

        cs=CastSerializer(data=data)
        if cs.is_valid():
            cs.save()
            return Response(cs.data,status=status.HTTP_200_OK)
        else:
            return Response(cs.errors,status=status.HTTP_400_BAD_REQUEST)


class List_Movies(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            movie_data=MovieModel.objects.all()
            ms=MovieSerializer(movie_data,many=True)
            return Response(ms.data,status=status.HTTP_200_OK)
        except MovieModel.DoesNotExist:
            content={"error":"No movies List"}
            return Response(content,status=status.HTTP_404_NOT_FOUND)



class Movie_Details(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        try:
            mdata=MovieModel.objects.get(pk=id)
            ms=MovieSerializer(mdata)
            return Response(ms.data,status=status.HTTP_200_OK)
        except MovieModel.DoesNotExist:
            content={'error':"Movie Doesn't exists"}
            return Response(content,status=status.HTTP_404_NOT_FOUND)