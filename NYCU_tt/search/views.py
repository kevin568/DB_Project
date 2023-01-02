from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
def home(request):
    return render(request, "search/home.html")