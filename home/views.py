from django.shortcuts import render
from .models import Project
from .models import Post
# Create your views here.
def home(request):
    projects = Project.objects.order_by('-project_year')[:3]
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'home.html', {'projects':projects, 'posts':posts})
