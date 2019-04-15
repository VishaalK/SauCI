from django.urls import path

from . import views

app_name = 'builds'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:build_id>/', views.detail, name='detail'),
]