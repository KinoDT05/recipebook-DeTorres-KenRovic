from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomView(LoginRequiredMixin, TemplateView):
    template_name = ""
    redirect_field_name = ''
# Create your views here.
