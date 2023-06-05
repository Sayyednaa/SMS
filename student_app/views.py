from django.shortcuts import render,redirect
from todo.models import Task
from django.contrib import messages
from django.contrib.auth.models import User
from pyislam import Quran
from django.contrib.auth import authenticate, login,logout
from .import pygq
import os
from todo.models import Task,syallbuss
from books.models import PwLecs
import random
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import matplotlib.pyplot as plt
import numpy as np
from django.views.decorators.csrf import csrf_protect,csrf_exempt



Q = pygq.PyGQ()

@user_passes_test(lambda u: u.is_superuser)
@login_required
def home(request):
   






    ayat=random.randint(1,280)
   
   
    # ayah=f'{Q.getAyah(2, ayat, "en.sahih")["verse"]} (2,{ayat})'
    ayah="بسم الله"
    if request.user.is_authenticated:
        x = datetime.date.today()
        date=x.strftime('%m/%d/%Y')
        print(date)
        lecs=PwLecs.objects.filter(Date=date)
        task=Task.objects.filter(description=datetime.date.today())
        
    

        TaskData=Task.objects.all()
        completedTask=Task.objects.filter(completed=True).count()
        Tc=syallbuss.objects.all().count()
        CompletedC=syallbuss.objects.filter(completed=True).count()
        Rc=Tc-CompletedC
        ct=completedTask
        pt=TaskData.count()-completedTask
      
       
        # plt.legend()
        # figpath="static/img/graphs/todograph.png"
        # os.system("del static\\img\\graphs\\")
        # plt.savefig(figpath)
    
        return render(request, 'main/home.html',{'totalTask':TaskData.count(),
                                                'completedTask':completedTask,
                                                'pendingTask':TaskData.count()-completedTask,
                                                'ayat':ayah,
                                                'task':task,
                                                'Tc':Tc,
                                                'CompletedC':CompletedC,
                                                'Rc':Rc,
                                                'lecs':lecs
                                                
                                                })
    return redirect("/login")

@csrf_exempt
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
           
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid Email or Password')
    return render(request,'main/login.html')

@login_required
def logoutUser(request):
   logout(request)
   return redirect('/login')


def forgetPass(request):
    pass
def createac(request):
    if request.user.is_authenticated:
      
        return redirect('/')
    if request.method=='POST':
            print("hurray")
            password=request.POST['password']
            username=request.POST['username']
            email=request.POST['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, 'Account Created Successfully')
      
    return render(request,'main/signup.html')