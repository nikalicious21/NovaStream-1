# ////////////// IMPORTS //////////////////////////////////////
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# /////////////////////////////////////////////////////////////


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(
        blank=False
    )
    photoUrl = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField(auto_now_add=True)