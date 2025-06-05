from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from todo_user.models import TODOO

# function for rendering the home page template and handling user signup
def home(request):
    if request.method=='POST':
        username = request.POST.get('fnm')
        password =  request.POST.get('pwd')
        email = request.POST.get('emailid')
        my_user = User.objects.create_user(username=username, password=password, email=email)
        my_user.save()
        return redirect("home")
    else:
        return render(request,'signup.html')
    
# function for rendering the login page template
# Note: This function currently does not handle authentication logic.
# It simply renders the login page template
def login(request):
    if request.method=='POST':
        username = request.POST.get('fnm')
        password = request.POST.get('pwd')

        if username and password:
            user = User.objects.get(username=username)
            check_password = user.check_password(password)
            if check_password:
                request.session['username'] = username
                return redirect("todo")
            else:
                return HttpResponse("Invalid credentials, please try again.")
        else:
            return HttpResponse("Please enter both username and password.")

    return render(request,'loginin.html')


def Todo(request):
    if request.method =='POST':
        title = request.POST.get('title')
        if title:
            user = User.objects.get(username=request.session.get('username'))
            todo_item = TODOO(title=title, user=user)
            todo_item.save()
            return redirect("todo")
        else:
            return HttpResponse("Please enter a title for your todo item.")
    else:
        username = request.session.get('username')
        if username:
            usr_id = User.objects.get(username=username)
            todo_items = TODOO.objects.filter(user=usr_id)
            context = {'res':todo_items,'username': username}
            return render(request, "todo.html", context)


def signout(request):
    return redirect("home")

def edit_todo(request, srno):
    if request.method == 'POST':
        Todoo_item = TODOO.objects.get(srno=srno)
        Todoo_item.title = request.POST.get('title')
        Todoo_item.user = request.user
        Todoo_item.save()
        return redirect("todo")
    else:
        Todoo_item = TODOO.objects.filter(srno=srno)
        context = {'res': Todoo_item}
        return render(request, "edit.html", context)

        
def delete_todo(request, srno):
    Todoo_item = TODOO.objects.get(srno=srno)
    Todoo_item.delete()
    return redirect("todo")