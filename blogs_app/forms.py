from django.forms import ModelForm
from .models import Blogs
from django.contrib.auth.models import User


class CreateBlogForm(ModelForm):
    
    class Meta:
        model = Blogs
        fields = '__all__'