from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from .models import Build
# Create your views here.

def index(request):
    builds = Build.objects.order_by('-completed_at')[:5]
    return render(request, 'builds/index.html', {'builds': builds})

def detail(request, build_id):
    build = get_object_or_404(Build, pk=build_id)
    return render(request, 'builds/detail.html', {'build': build})

