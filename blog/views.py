from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogobjects = Blog.objects.order_by("-blog_date")[:5]
    
    return render(request, "blog/all_blogs.html", {"blogobjects":blogobjects})