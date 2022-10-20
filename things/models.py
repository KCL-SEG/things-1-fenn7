import django
from enum import unique
from wsgiref.validate import validator
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Thing(models.Model):
    name=models.CharField(
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
        blank=True,
    )
    
    quantity = models.IntegerField(
        unique=False,
        validators=[
            MinValueValidator(0, message = "Value must be bigger than 0!"),
            MaxValueValidator(100, message = "Value must be less than 100!")
                    ]
    )
