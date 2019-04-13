from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import Build
# Create your views here.

def index(request):
    builds = Build.objects.all()
    response = "You're looking at ids %s"
    ids = ', '.join([str(build.id) for build in builds])
    return HttpResponse(response % ids)

def detail(request, build_id):
    build = Build.objects.get(pk=build_id)
    context = {'build': build}
    return render(request, 'builds/detail.html', context)

