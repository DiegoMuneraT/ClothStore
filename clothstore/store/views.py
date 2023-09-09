from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/nosotros.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contacto.html'

class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'

