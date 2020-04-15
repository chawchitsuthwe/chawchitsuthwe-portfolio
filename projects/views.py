from django.shortcuts import render, get_object_or_404
from .models import Project,Gallery
# Create your views here.
def projects(request):
    projects = Project.objects
    return render(request, 'projects/projects.html', {'projects':projects})

def project_detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    gallerys = Gallery.objects.filter(project=project_detail)
    return render(request, 'projects/project_detail.html', {'project':project_detail, 'gallerys':gallerys})
