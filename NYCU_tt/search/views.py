from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
def show(request):
    courses = Course.objects.all()
    return render(request, "search/show.html", {"courses":courses})