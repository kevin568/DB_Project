from django import forms
from .models import *
import django_filters

class CourseFilter(django_filters.FilterSet):
    courseName = django_filters.CharFilter(
        lookup_expr = 'icontains',
        widget = forms.TextInput(attrs={'class':'form-control'})
    )

    professor = django_filters.CharFilter(
        lookup_expr = 'icontains',
        widget = forms.TextInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = Course
        fields = '__all__'
