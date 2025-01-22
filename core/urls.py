from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='indes'),
    path('about/', views.about, name='about'),
]