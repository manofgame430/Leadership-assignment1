from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(request:HttpRequest)->HttpResponse:
    context = {"teams": ["procurment", "management", "community", "documentation"]}
    return render(request, 'home.html', context)

def procurment_view(request:HttpRequest)->HttpResponse:
    context = {"members": ["Christopher", "Tristan", "Brian"]}
    return render(request, 'procurment.html', context)

def management_view(request:HttpRequest)->HttpResponse:
    context = {"members": ["Christopher", "Tristan", "Brian"]}
    return render(request, 'management.html', context)

def community_view(request:HttpRequest)->HttpResponse:
    context = {"members": ["Germaine", "Tyler Vincent", "Tyler Joy", "Corey"]}
    return render(request, 'community.html', context)

def documentation_view(request:HttpRequest)->HttpResponse:
    context = {"members": ["Germaine", "Tyler Vincent", "Tyler Joy", "Corey"]}
    return render(request, 'documentation.html', context)