from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Task
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def login_page(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have Sucessfully Loged")
            return redirect('/')
        else:
            messages.success(request,"Invalid Creditial")
            return redirect('/login') 
    return render(request,"login.html")

def home(request):
    if request.user.is_staff:
        tasks=Task.objects.all().order_by('user_profile')
    else:

        tasks=Task.objects.filter(user_profile=request.user.id)
    context={
        'tasks':tasks
    }
    return render(request,"home.html",context)

def log_out(request):
    logout(request)
    messages.success(request,"Log Out Sucessfully Login Again")
    return redirect('/')

def add_record(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            tittle=request.POST['tittle']
            disc=request.POST['disc']
            Task.objects.create(Tittle=tittle,discription=disc,user_profile=request.user)
            messages.success(request,"Reecord Added")
            return redirect('/')
    else:
        return redirect("/login")
    return render(request,"records/add_record.html")

def update_record(request,pk):
    if request.user.is_authenticated:
        task=Task.objects.get(id=pk)
        context={
            'task':task
        }
        if request.method=="POST":
            tittle=request.POST['tittle']
            disc=request.POST['disc']
            obj=Task.objects.get(id=pk)
            obj.Tittle=tittle
            obj.discription=disc
            obj.save()
            messages.success(request," Record Updated")
            return redirect("/")
    else:
        return redirect("/login")
    return render(request,"records/update_record.html",context)

def delete_record(request,pk):
    if request.user.is_authenticated:
        obj=Task.objects.get(id=pk)
        obj.delete()
        messages.success(request,"Task Deleted")
        return redirect("/")
    else:
        return redirect("/login")

def record_view(request,pk):
    if request.user.is_authenticated:
        tasks=Task.objects.get(id=pk)
        context={
            'tasks':tasks
        }
    else:
        return redirect("/login")
    return render(request,"records/record_details.html",context)

def registration(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered sucessfully")
            return redirect("/login")
        else:
            messages.error(request,"Somthing went Wrong try again")
            return render(request,"registration.html",{'form':form})
    else:
        form=CustomUserCreationForm()
        return render(request,"registration.html",{'form':form})
    
def list_users(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            list_users=User.objects.all()
            context={
                'list_users':list_users
            }
        else:
            return redirect('/')
    else:
        return redirect("/login")

    return render(request,"users.html",context)

def user_tasks(request,pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            tasks=Task.objects.filter(user_profile_id=pk)
            context={
                'tasks':tasks
            }
            print(context)
        else:
            return render("/")
    else:
        return render("/login")

    return render(request, "records/user_tasks.html",context)

def search(request):
    if request.user.is_authenticated:
        data=request.GET['search']
        if request.user.is_staff:
            tasks=Task.objects.filter(Tittle__icontains=data)
        else:
            tasks=Task.objects.filter(user_profile=request.user.id , Tittle__icontains=data)
        context={
            'tasks':tasks
        }
    else:
        return redirect("/login")
    return render(request,"records/search_records.html",context)