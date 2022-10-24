from django.shortcuts import render, redirect
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.views.generic import  TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from blogs_app.models import Blogs
blogs = Blogs.objects.all()
# Class Based Views
class HomePageView(TemplateView):
    template_name = 'home_app/home_page.html'
    extra_context = {'today': datetime.today(), 'blogs': blogs}



# Function Based Views
# def home_page(request):
#     today = datetime.today()
#     return render(request, 'home_app/home_page.html', context={'today': today,})


@login_required(login_url='/admin/')
def userAdminPage(request):
    return render(request, 'home_app/user.html', {})



