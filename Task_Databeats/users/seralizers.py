from rest_framework import serializers
from users.models import Register,CastModel,MovieModel

class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model=Register
        fields='__all__'


class CastSerializer(serializers.ModelSerializer):

    class Meta:
        model = CastModel
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    casts=CastSerializer(many=True,read_only=True)


    class Meta:
        model=MovieModel
        fields=['id','title','created_at','updated_at','runtime','language','tagline','casts']












