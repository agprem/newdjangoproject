from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def check_Info(request):
    #data="<html><h1>Welcome to Profile-App's Info </h1><br><br><br><pre><h3> Info      Contact Person</h3></pre></html>"
    #return HttpResponse(data)
    return render(request,'info.html')

def check_ContactPerson(request):
    #data="<html><h1>Welcome to Profile-App's Contact Person </h1><br><br><br><pre><h3> Info    Contact Person</h3></pre></html>"
    #return HttpResponse(data)
    return render  (request,'settings.html')
