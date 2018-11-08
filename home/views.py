from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
app_name = 'home'
class AboutPage(TemplateView):
    template_name = 'home/about.html'

class HomePage(TemplateView):
    template_name = 'base.html'
