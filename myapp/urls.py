from django.urls import path
from . import views


urlpatterns = [
    path('postcomment', views.postComment, name='postcomment'),
    path('', views.bloghome, name='bloghome'),
    path('<str:slug>', views.blogpost, name='blogpost'),



]