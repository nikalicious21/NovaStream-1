# ////////////// IMPORTS //////////////////////////////////////
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# /////////////////////////////////////////////////////////////


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
<<<<<<< HEAD
    content = models.TextField()
    photoUrl = models.CharField(max_length=100)
    videoUrl = models.CharField(max_length=100)
=======
    content = models.TextField(blank=True)
    imageUrl = models.CharField(max_length=100, blank=True)
    videoUrl = models.CharField(max_length=100, blank=True)
>>>>>>> 66c4aaf8e06751dc0a4c32a4e75efcf81023e8f9
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # sources = 
    datePublished = models.DateTimeField(auto_now_add=True)