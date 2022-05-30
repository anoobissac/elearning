from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView) :
    template_name='master/home.html'
    extra_context={
         'title':'home',
         
    }

class AboutUsView(TemplateView):
    template_name="master/about_us.html"
    extra_context={
        'title':'About Us'
    }

class ContactUsView(TemplateView):
    template_name='master/contact_us.html'
    extra_context={
        'title':'Contact Us'
    }