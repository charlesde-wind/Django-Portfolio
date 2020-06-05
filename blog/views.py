from django.shortcuts import render, get_object_or_404
from .models import Blog
from functools import reduce

# Create your views here.
def all_blogs(request):
    blogobjects = Blog.objects.order_by("-blog_date")[:5]
    all_blogs = Blog.objects.all()
    
    count = 0
    for i in range(len(all_blogs)):
        count+=1
    
    return render(request, "blog/all_blogs.html", {"blogobjects":blogobjects, "owner":"Charles De-Wind","noofblogs":count})

# def detail(request, blog_id):
#     try:
#         blogObj = Blog.objects.order_by("-blog_date")[blog_id-1]
        
#         return render(request, "blog/detail.html", {"id":blogObj})
    
#     except Exception:
#         blogobjects = Blog.objects.order_by("-blog_date")[:5]
#         return render(request, "blog/all_blogs.html", {"blogobjects":blogobjects})

def detail(request, blog_id):
    blog= get_object_or_404(Blog, pk=blog_id)
    
    return render(request, "blog/detail.html", {"blog":blog})