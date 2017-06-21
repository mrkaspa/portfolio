from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from .models import Project
from .forms import ContactForm


@require_GET
def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})


@require_GET
def project_by_id(request, id=''):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'projects/show.html', {'project': project})


@require_GET
def show_headers(request):
    res = map(lambda t: f"<li>{t[0]} = {t[1]}</li>", request.META.items())
    return HttpResponse("<ul>{}</ul>".format('\n'.join(res)))


@require_GET
def show_get(request):
    res = map(lambda t: f"<li>{t[0]} = {t[1]}</li>", request.GET.items())
    return HttpResponse("<ul>{}</ul>".format('\n'.join(res)))


@require_GET
def contact(request):
    f = ContactForm()
    return render(request, 'form.html', {'form': f})


@require_POST
def save_contact(request):
    f = ContactForm(request.POST)
    if f.is_valid():
        cd = f.cleaned_data
        res = map(lambda t: f"<li>{t[0]} = {t[1]}</li>", cd.items())
        return HttpResponse("<ul>{}</ul>".format('\n'.join(res)))
    else:
        f = ContactForm()
        return render(request, 'form.html', {'form': f})
