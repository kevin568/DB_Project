from django.db import models

# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length = 30)
    professor = models.CharField(max_length = 10)
    semester = models.CharField(max_length = 20)
    time = models.CharField(max_length = 10)
    credit = models.DecimalField(max_digits = 2, decimal_places = 0)

class Experience(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = 'experience')
    exp = models.TextField(blank = False)
    recommand = models.DecimalField(max_digits = 1, decimal_places = 0)

class Content(models.Model):
    gradindpolicy = models.TextField(blank = False)
    classMethod = models.TextField(blank = False)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = 'content')