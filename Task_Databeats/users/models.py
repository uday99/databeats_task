from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Register(AbstractBaseUser):
    objects=UserManager()

    username=models.CharField(max_length=150,unique=True)
    email=models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class MovieModel(models.Model):
    title=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    runtime=models.IntegerField()
    language=models.CharField(max_length=100)
    tagline=models.CharField(max_length=100)



class CastModel(models.Model):
    Gender_Choice=(
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    )
    movie=models.ForeignKey(MovieModel,on_delete=models.CASCADE,related_name='casts')
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=3,choices=Gender_Choice)
    dob=models.DateField()
