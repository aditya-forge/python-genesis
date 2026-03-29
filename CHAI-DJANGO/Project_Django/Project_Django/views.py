from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    # return HttpResponse("Hi Home Page")
    return render(request,'website/index.html')

