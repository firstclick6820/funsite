from django.contrib import admin


from .models import Profile, SocialMedai, UserBasicInfo
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    
    
    
@admin.register(SocialMedai)
class SocialMediaAdmin(admin.ModelAdmin):
    model = SocialMedai
    
    
    
@admin.register(UserBasicInfo)
class UserBasicInfoAdmin(admin.ModelAdmin):
    model = UserBasicInfo