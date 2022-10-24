from email.policy import default
from hashlib import blake2b
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    bio = models.CharField(max_length=240, blank=True)
    about= models.TextField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="static/images/user")
    
    
    
    def __str__(self):
        return self.user.get_username()
    
    


class SocialMedai(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    website = models.URLField(blank=True)
    instagram= models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter=models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.user.get_username()
    
    

class UserBasicInfo(models.Model):
    GENDER_MALE = 'MALE'
    GENDER_FEMALE = 'FEMALE'
    
    GENDER_CHOICES = {
        (GENDER_MALE, 'M'),
        (GENDER_FEMALE, 'F')
    }
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=100)
    gender = models.TextField(GENDER_CHOICES, default=GENDER_MALE)
    verified = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.user.get_username()