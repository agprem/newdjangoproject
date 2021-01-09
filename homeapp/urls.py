from django.contrib import admin
from django.urls import path
from homeapp import views


urlpatterns = [
    path('',views.homepage),
    path('profile/',views.check_profile),
    path('setting/',views.check_settings),
    path('contactus/',views.check_contactus),

]
