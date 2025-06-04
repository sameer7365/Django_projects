from django.http import HttpResponse
from django.shortcuts import render
from todos.models import TodoItem, Task


def home(request):
      # Clear all tasks for demonstration purposes
    print("Task.objects.all()",Task.objects.all())
    completed_tasks = TodoItem.objects.filter(completed=True)
    print("completed_tasks !!!!!!####", completed_tasks)

    context = {'todo_items': TodoItem.objects.filter(completed=False).order_by('-updated_at'),
               'tasks':Task.objects.all(),"completed_tasks": completed_tasks}
    return render(request, 'todo.html', context)
