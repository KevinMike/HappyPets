from django.shortcuts import render
from django.http import  HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponseRedirect("/admin/")
    #return render(request,'index.html')

def login(request):
    return render(request,'login.html')