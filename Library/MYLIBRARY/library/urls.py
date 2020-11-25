from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_detail/<str:id>/', views.book_detail, name='book_detail'),
    path('book_request/<str:id>/', views.book_request, name='book_request'),
    path('profile_details',views.profile_details,name='profile_details'),
    path('book_return/', views.book_return, name='book_return'),
]
