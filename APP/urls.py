from django.contrib import admin 
from django.urls import path
from APP import views
urlpatterns = [
    path('', views.Home, name="Home"),
    path('login/', views.login, name='login'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('vote/', views.vote, name="vote"),
    path('participate/', views.participate, name='participate'),
    path('profile/', views.profile, name="profile"),
    path('forgotpassword/', views.forgotpassword , name="forgotpassword"),
    path('register/', views.register, name="register"),
    path('createpage/', views.createpage, name="createpage"),
    path('create/', views.create, name="create"),
    path('manage/', views.manage, name="manage"),
]