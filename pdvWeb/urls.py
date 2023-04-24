from django.contrib import admin
from django.urls import path, include, re_path
from .views import pdvWeb

app_name = 'pdvWeb'

urlpatterns = [
        path('', pdvWeb, name='pdvWeb'),
    
]