from django.urls import path
from master.views import  HomeView,AboutUsView,ContactUsView

urlpatterns=[
    path("",HomeView.as_view(),name="home"),
    #path("hello_world",hello_world,name="hello_world"),
    #path('about_us',about_us_view,name='about_us'),
    path('about_us',AboutUsView.as_view(),name='about_us'),
    #path('contact_us',contact_us_view,name="contact_us")
    path('contact_us',ContactUsView.as_view(),name='contact_us')
]