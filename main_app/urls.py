# ////////// IMPORTS //////////////////////
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_index, name="index"),
    path('about/', views.about, name="about"),
    path('signup', views.signup, name='signup'),
]