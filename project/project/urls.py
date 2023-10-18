from pipes import Template
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import urls
from django.views.generic import TemplateView
from app.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='home.html'),name='home_page'),
    path('users/',include('django.contrib.auth.urls')),
    path('register/',Register.as_view(),name='register_page')
]
