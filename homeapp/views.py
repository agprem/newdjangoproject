from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def homepage(request):
    #data="<html><h1>Welcome to Homeapps Profile </h1><br><br><br><pre><h3> Profile    Settings     Contact us </h3></pre></html>"
    #return HttpResponse(data)
    return render(request,'home.html')

def check_profile(request):
    #data="<html><h1>Welcome to Homeapps Profile </h1><br><br><br><pre><h3> Profile    Settings     Contact us </h3></pre></html>"
    #return HttpResponse(data)
    return render(request,'profile.html')
def check_settings(request):
    #data="<html><h1>Welcome to Homeapps Settings </h1><br><br><br><pre><h3> Profile    Settings     Contact us </h3></pre></html>"
    #return HttpResponse(data)
    return render(request, 'setting.html')
def check_contactus(request):
    #data="<html><h1>Welcome to Homeapps Contact us </h1><br><br><br><pre><h3> Profile    Settings     Contact us </h3></pre></html>"
    #return HttpResponse(data)
    return render(request, 'contact.html')
