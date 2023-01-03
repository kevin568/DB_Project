from django.contrib import admin
from .models import *

# Register your models here.
class Course_Admin(admin.ModelAdmin):
    list_display = ('id', 'courseName', 'professor', 'semester', 'time', 'credit')

class Response_Admin(admin.ModelAdmin):
    list_display = ('id', 'course', 'gradindpolicy', 'classMethod', 'resp', 'recommand')

'''
class Experience_Admin(admin.ModelAdmin):
    list_display = ('id', 'course', 'exp', 'recommand')

class Content_Admin(admin.ModelAdmin):
    list_display = ('id', 'course', 'gradindpolicy', 'classMethod')
'''

admin.site.register(Course, Course_Admin)
admin.site.register(Response, Response_Admin)
#admin.site.register(Experience, Experience_Admin)
#admin.site.register(Content, Content_Admin)