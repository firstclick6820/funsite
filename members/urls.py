from django.urls import path
from . import views

urlpatterns = [
    path('login', views.member_login, name='member_login'),
    path('register', views.memeber_register, name='member_register'),
    path('logout', views.member_logout, name='member_logout'),
    path('user_dashboard/<int:id>', views.user_dashboard, name='user_dashboard'),
    path('user_profile/<int:id>',views.user_profile, name='user_profile')
]
