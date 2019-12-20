# ////////////// IMPORTS //////////////////////////////////////
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# /////////////////////////////////////////////////////////////


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    imageUrl = models.CharField(max_length=100)
    videoUrl = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # sources = 
    datePublished = models.DateTimeField(auto_now_add=True)