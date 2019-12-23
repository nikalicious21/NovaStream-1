#  ////////////////// IMPORTS //////////////////////////////////////
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Post, Photo, Image
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid
from datetime import date
from django.utils import timezone

# Make sure to add your bucket name below
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com'
BUCKET = ''

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

@login_required  
def profile(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'posts': posts})

@login_required
def add_image(request, post_id):
    img_file = request.FILES.get('img-file', None)
    if img_file:
        s3 = boto3.client('s3')
        file_extension = img_file.name[img_file.name.rfind('.') :]
        key = uuid.uuid4().hex[:6] + file_extension

        try:
            s3.upload_fileobj(img_file, BUCKET, key)
            url = f"{S3_BASE_URL}/{BUCKET}/{key}"
            post = Post.objects.get(pk=post_id)
            post.imageUrl = url
            post.save()
        except:
            print('add_image() Failed. Error while uploading file to S3')
    return redirect('post_detail', post_id)

@login_required
def add_photo(request, user_id):
    img_file = request.FILES.get('img-file', None)
    if img_file:
        s3 = boto3.client('s3')
        file_extension = img_file.name[img_file.name.rfind('.') :]
        key = uuid.uuid4().hex[:6] + file_extension

        try:
            s3.upload_fileobj(img_file, BUCKET, key)
            url = f"{S3_BASE_URL}/{BUCKET}/{key}"
            photo = Photo(url=url, user_id=user_id)
            photo.save()
        except:
            print('add_photo() Failed. Error while uploading file to S3')
    return redirect('profile')


@login_required
def remove_photo(request, photo_id):
    user = request.user
    photo = Photo.objects.get(pk=photo_id)
    photo.delete()
    return redirect('/profile/')

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