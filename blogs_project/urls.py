import django.contrib.auth.urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('blogs/', include('blogs_app.urls')),
    path('notes/', include('notes_app.urls')),
    path('member/', include(django.contrib.auth.urls)),
    path('member/', include('members.urls')),

]
