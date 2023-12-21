from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('topics/', views.topics, name='topics'),
    path('activities/', views.activities, name='activites'),
    path('profile/<str:pk>/', views.userprofile, name='userprofile'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create_room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteROOm, name='delete-room'),
    path('delete-message/<str:pk>/', views.deletemessage, name='delete-message'),
    path('update-user/', views.updateuser, name='update-user')
]