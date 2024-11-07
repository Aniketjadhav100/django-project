# /home/ubuntu/my_django_project/src/my_django_project/urls.py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

