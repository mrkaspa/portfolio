from django.shortcuts import render, get_object_or_404
from web.models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})


def project_by_id(request, id=''):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'projects/show.html', {'project': project})
