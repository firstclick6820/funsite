from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from blogs_app.models import Blogs
from . forms import CustomUserCreationForm

# login a user
def member_login(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You are already logged in.')
        return redirect('home_app')
    
    
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.add_message(request, messages.SUCCESS, 'You have logged in successfully.')
            login(request, user)
            return redirect('user_dashboard', id=user.id)
        else:
            return redirect('member_login')
        
    
    else: 
        return render(request, 'members/authenticate/login.html')
    
    
    
    
    
# register a user
def memeber_register(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You are already logged in.')
        return redirect('home_app')
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Your account created successfully')
            return redirect('home_app')
        else:
            messages.add_message(request, messages.WARNING, 'Something went wrong, try again!')
    else:
        form = CustomUserCreationForm()
        
        context= {'form': form}
        return render(request, 'members/authenticate/register.html', context)
    
    



def member_logout(request):
    logout(request)
    return render(request, 'members/authenticate/logout.html')







@login_required(login_url='member_login')
def user_dashboard(request, id):
    user_blogs = Blogs.objects.filter(author__id = id)
    
    
    
    context = {'blogs': user_blogs}
    return render(request, 'members/user/user_dashboard.html',context)



@login_required(login_url='member_login')
def user_profile(request, id):
    user = User.objects.get(pk=id)
    context = {'user':user }
    return render(request, 'members/user/user_profile.html',context)