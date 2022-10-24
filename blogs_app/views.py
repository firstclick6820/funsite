from http.client import HTTPResponse
from django.http import FileResponse
from django.shortcuts import render, redirect
from .models import Blogs
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.db.models.aggregates import Count
from .forms import CreateBlogForm



import io
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Image, PageBreak
from reportlab.lib.pagesizes import A4




# class BlogsListView(ListView):
#     success_url = 'blog_list'
#     model = Blogs
#     template_name = 'blogs_app/blogs_list.html'
#     context_object_name = 'blogs'


# class BlogDetailsViwe( DetailView):

#     model = Blogs
#     template_name = 'blogs_app/blog_details.html'
#     context_object_name = 'blog'
    
    
# Blogs List All ...............................................................................................

# All Blogs
def blogs_list(request):
    blogs_list = Blogs.objects.filter(status=1).order_by('created_on')
    blogs_count = Blogs.objects.filter(status=1).aggregate(blogs=Count('id'))
    return render(request, 'blogs_app/blogs_list.html', context={'blogs': blogs_list, 'blogs_count': blogs_count})

# Today Blog Filter
def today_blogs(request):
    from datetime import date
    today = date.today()
    blogs_list = Blogs.objects.filter(created_on__icontains=today).all()
    blogs_count = Blogs.objects.filter(created_on__icontains=today).filter(status=1).aggregate(blogs=Count('id'))
    context = {'blogs': blogs_list, 'blogs_count': blogs_count}
    return render(request, 'blogs_app/blogs_list.html', context)

#This Week Blogs Filter
def this_week_blogs(request):
    from datetime import datetime, timedelta
    one_week_ago = datetime.today() - timedelta(days=7)
    blogs_list = Blogs.objects.filter(created_on__gte=one_week_ago).all()
    blogs_count = Blogs.objects.filter(created_on__gte=one_week_ago).filter(status=1).aggregate(blogs=Count('id'))
    context = {'blogs': blogs_list, 'blogs_count': blogs_count}
    return render(request, 'blogs_app/blogs_list.html', context)

#This Month Blogs Filter
def this_month_blogs(request):
    from datetime import datetime, timedelta
    one_month_ago = datetime.today() - timedelta(days=30)
    blogs_list = Blogs.objects.filter(created_on__gte=one_month_ago).all()
    blogs_count = Blogs.objects.filter(created_on__gte=one_month_ago).filter(status=1).aggregate(blogs=Count('id'))
    context = {'blogs': blogs_list, 'blogs_count': blogs_count}
    return render(request, 'blogs_app/blogs_list.html', context)

#This Year Blogs Filter
def this_year_blogs(request):
    from datetime import datetime, timedelta
    one_year_ago = datetime.today() - timedelta(days=365)
    blogs_list = Blogs.objects.filter(created_on__gte=one_year_ago).all()
    blogs_count = Blogs.objects.filter(created_on__gte=one_year_ago).filter(status=1).aggregate(blogs=Count('id'))
    context = {'blogs': blogs_list, 'blogs_count': blogs_count}
    return render(request, 'blogs_app/blogs_list.html', context)

# Retrieving Draft Posts
def draft_posts(request):
    blogs_list = Blogs.objects.filter(status=0).order_by('-created_on')
    blogs_count = Blogs.objects.filter(status=0).aggregate(blogs=Count('id'))
    return render(request, 'blogs_app/blogs_list.html', context={'blogs': blogs_list, 'blogs_count': blogs_count})

# Blogs List End..............................................................................................................

#View Single Blog
def blog_detials(request, pk):
    blog = Blogs.objects.get(pk=pk)
    return render(request, 'blogs_app/blog_details.html', context={'blog': blog})


#Create A Blog
def create_blog(request):
    if request.method =="POST":
        form = CreateBlogForm(request.POST, initial={'user': request.user})
        return HTTPResponse(form)
        if form.is_valid():
            new_blog = form.save()
            return redirect('blog_list')
        else:
            messages.add_message(request, messages.WARNING, 'Something went wrong, try again!')
            return 
    else:
        return render(request, 'blogs_app/create_blog.html')



















@login_required(login_url='member_login')
def blogViewPdf(request, pk):
    blog= Blogs.objects.get(pk=pk)

    pdf_buffer = io.BytesIO()
    my_doc = SimpleDocTemplate(pdf_buffer, pagesizes=A4)
    
    flowables = []
    
    sample_style_sheet = getSampleStyleSheet()
    
    blog_title = Paragraph(blog.title, sample_style_sheet['Heading1'])
    blog_body = Paragraph(blog.content, sample_style_sheet['BodyText'])
    
    
    flowables.append(blog_title)
    flowables.append(blog_body)
    # flowables.append(Image(blog.image))
    # flowables.append(PageBreak())
    
    
    my_doc.build(flowables)
    pdf_buffer.seek(0)

    return FileResponse(pdf_buffer, as_attachment=False, filename=f'{blog.title}.pdf')




@login_required(login_url='member_login')
def blogGetPdf(request, pk):
    blog= Blogs.objects.get(pk=pk)

    pdf_buffer = io.BytesIO()
    my_doc = SimpleDocTemplate(pdf_buffer, pagesizes=A4)
    
    flowables = []
    
    sample_style_sheet = getSampleStyleSheet()
    
    blog_title = Paragraph(blog.title, sample_style_sheet['Heading1'])
    blog_body = Paragraph(blog.content, sample_style_sheet['BodyText'])
    
    
    
    flowables.append(blog_title)
    flowables.append(blog_body)

    
    my_doc.build(flowables)
    

    pdf_buffer.seek(0)

    return FileResponse(pdf_buffer, as_attachment=True, filename=f'{blog.title}.pdf')





def delete_all_blogs(request):
    if request.method == "POST":
        blogs = Blogs.objects.all().delete()
        messages.add_message(request, messages.SUCCESS, 'All blogs are deleted succeessfully!')
        return redirect('blog_list')
    else:
        return render(request, 'blogs_app/delete_all_blogs.html')