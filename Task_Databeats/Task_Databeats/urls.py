"""Task_Databeats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/user/',views.Register_User.as_view(),name='reg_user'),
    path('user/login/',views.User_Login.as_view(),name='user_login'),
    #
    path('create/movie/',views.Create_Movie.as_view(),name='create_mv'),
    path('create/cast/',views.Cast_Movie.as_view(),name='cast_movie'),

    path('movies/',views.List_Movies.as_view(),name='movies'),
    path('movie/<int:id>/',views.Movie_Details.as_view(),name='movie_info')
]
