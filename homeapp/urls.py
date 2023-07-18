from django.urls import path
from . import views
from .views import AddBlog

urlpatterns=[
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('signup', views.handelsignup, name='handelsignup'),
    path('login', views.handellogin, name='handellogin'),
    path('logout', views.handellogout, name='handelogout'),
    path('addblog/', AddBlog.as_view(), name='addblog'),
]