from enum import unique
from wsgiref.validate import validator
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Thing(AbstractUser):
    username=models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        validators=[RegexValidator(
            message="Usernames must be unqiue, "
        )]
    )
    
    description = models.TextField(
        max_length=120,
        unique=False,
        blank=False,
    )
    
    quantity = models.IntegerField(
        max_length=100,
        blank=False,
        validators=[
            MinLengthValidator(0, message = "Value must be bigger than 0!"),
            MaxLengthValidator(100, message = "Value must be less than 100!")
                    ]
    )
