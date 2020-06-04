from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projectsObj = Project.objects.all()
    
    return render(request, "portfolio/index.html", {"projects":projectsObj})