from django.contrib import admin
from .models import *

# Register your models here.
class Course_Admin(admin.ModelAdmin):
    list_display = ('id', 'courseName', 'professor', 'semester', 'time', 'credit')

class Experience_Admin(admin.ModelAdmin):
    list_display = ('course', 'exp', 'recommand')

class Content_Admin(admin.ModelAdmin):
    list_display = ('course', 'gradindpolicy', 'classMethod')

admin.site.register(Course, Course_Admin)
admin.site.register(Experience, Experience_Admin)
admin.site.register(Content, Content_Admin)