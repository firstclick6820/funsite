from django.contrib import admin

from .models import Blogs, Tag



@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    model = Blogs
    
    list_display = ('title', 'slug', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag