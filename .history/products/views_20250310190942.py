from django.shortcuts import render
from django.views.generic import TemplateView




class Indexpage(TemplateView):
    template_name = "index.html"


