from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class BaseView(TemplateView):
    template_name = 'Base/index.html'

class HomeView(TemplateView):
    template_name = 'Home/index.html'

class ExpView(TemplateView):
    template_name = 'Experience/index.html'

class ProjView(TemplateView):
    template_name = 'Projects/index.html'

class SkillsView(TemplateView):
    template_name = 'Skills/index.html'

class AboutView(TemplateView):
    template_name = 'About/index.html'