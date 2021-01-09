from django.contrib import admin
from django.urls import path
from profileapp import views

urlpatterns = [
    path('Information/',views.check_Info),
    path('ContactPerson/',views.check_ContactPerson),
    ]
