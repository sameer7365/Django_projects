from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # add task
    path('addtask/', views.addTask,name='add_task'),
    # mark as done
    path('Markdone/<int:pk>', views.Markdone,name='mark_done'),
    # mark as undone
    path('Markundone/<int:pk>', views.Markundone,name='mark_undone'),
    # edit task
    path('Edit/<int:pk>', views.Edit,name='edit_task'),
    #delete task
    path('Deletetask/<int:pk>', views.Deletetask,name='delete_task'),


]