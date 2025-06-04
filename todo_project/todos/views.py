from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from todos.models import TodoItem,Task
# from .models import TodoItem


def addTask(request):
    title = request.POST.get('task')
    task_selection_id = request.POST.get('task_selection')
    val_obj = Task.objects.get(id=task_selection_id)
    TodoItem.objects.create(
        title=title,project=val_obj)
    return redirect("home")


def Markdone(request, pk):
    print("Markdone called with pk:", pk)
    value_get = TodoItem.objects.get(id=pk)
    print("value_get:", value_get.completed)
    value_filter = TodoItem.objects.filter(id=pk)
    print("value_filter:", value_filter)
    value_get.completed = True
    value_get.save()
    return redirect("home")

def Markundone(request, pk):
    print("Markundone called with pk:", pk)
    val = TodoItem.objects.get(id=pk)
    val.completed = False
    val.save()
    return redirect("home")


def Edit(request, pk):
    print("edit called with pk:",pk)
    edit_obj = TodoItem.objects.get(id=pk)
    if request.method == 'POST':
        request_title = request.POST.get('task')
        print("request_title:", request_title)
        if request_title:
            edit_obj.title = request_title
            edit_obj.save()
            return redirect("home")
    else:
       
        context = {
            'edit_obj': edit_obj,}
        
        print("edit_obj:", edit_obj)
    return render(request, 'edit_todo.html',context)

def Deletetask(request, pk):
    print("Deletetask called with pk:", pk)
    TodoItem.objects.get(id=pk).delete()
    return redirect("home")








