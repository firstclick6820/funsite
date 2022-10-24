from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs_list, name='blog_list'),
    path('<int:pk>/', views.blog_detials, name='blog_details'),
    path('delete_all_blogs/', views.delete_all_blogs, name='delete_all_blogs'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('viewPdf/<int:pk>/', views.blogViewPdf, name='blog_view_pdf'),
    path('getPdf/<int:pk>/', views.blogGetPdf, name='blog_get_pdf'),
    path('today_blogs/', views.today_blogs, name='today_blogs'),
    path('this_week_blogs/', views.this_week_blogs, name='this_week_blogs'),
    path('this_month_blogs/', views.this_month_blogs, name='this_month_blogs'),
    path('this_year_blogs/', views.this_year_blogs, name='this_year_blogs'),
    path('draft_posts/', views.draft_posts, name='draft_posts')
]
