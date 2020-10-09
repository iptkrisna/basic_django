from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.template_views, name='template')
]