#  ////////////////// IMPORTS //////////////////////////////////////
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid
from datetime import date
from django.utils import timezone
# ///////////// Cloudinary Stuff ///////////
import cloudinary
import cloudinary.uploader
import cloudinary.api
# //////////////// USING .env BY TYPING my_key = os.environ['SECRET_KEY']
import os

# //////////////////////////////////////////////////////////////////


# Create your views here.
def signup(request):
    error_msg = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_msg = 'Invalid Credentials - Try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_msg': error_msg}
    return render(request, 'registration/signup.html', context)


def home_index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
<<<<<<< HEAD

@login_required
=======
    
>>>>>>> 66c4aaf8e06751dc0a4c32a4e75efcf81023e8f9
def profile(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'posts': posts})

class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'post_list'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'imageUrl', 'videoUrl']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.now()
        context['date_now'] = date.today().strftime('dd/mm/YYYY')
        return context

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'imageUrl', 'videoUrl']
    success_url = '/posts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.now()
        context['date_now'] = date.today().strftime('dd/mm/YYYY')
        return context

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'