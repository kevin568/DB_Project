from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .filters import CourseFilter

# Create your views here.
def home(request):
    course = Course.objects.all()
    resp = Response.objects.all()
    cf = CourseFilter(queryset = course)
    if request.method == "POST":
        cf = CourseFilter(request.POST, queryset = course)
    context={
        'cf':cf,
        'resp':resp
    }
    return render(request, "search/home.html", context)