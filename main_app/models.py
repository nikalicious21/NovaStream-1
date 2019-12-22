# ////////////// IMPORTS //////////////////////////////////////
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# /////////////////////////////////////////////////////////////


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    imageUrl = models.CharField(max_length=100, blank=True)
    videoUrl = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # sources = 
    datePublished = models.DateTimeField(auto_now_add=True)
    