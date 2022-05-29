from django.shortcuts import render
from django.http import HttpResponse
# from polls import template
# Create your views here.
def home_view(request,*args,**kwargs):
    mycontext={
        'names':['adham','amal','ahmed','hassan']
    }
    return render(request,'home.html',mycontext)

def home_view2(*args,**kwargs):
    return HttpResponse("<h1>Home Two </h1>")

def nothing(*args,**kwargs):
    return HttpResponse("<h1>Nothing</h1>")