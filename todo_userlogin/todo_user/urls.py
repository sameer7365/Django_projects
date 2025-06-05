from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.login,name='login'),
    path('todo', views.Todo, name='todo'),
    path('signout', views.signout, name='signout'),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>', views.delete_todo, name='edit_todo'),]
