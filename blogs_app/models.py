from argparse import BooleanOptionalAction
from distutils.command.upload import upload
from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    
    
    def __str__(self):
        return self.name



class Blogs(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    content = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    tags = models.ManyToManyField(Tag, blank=True)
    
    
    def __str__(self):
        return self.title
    
    
    