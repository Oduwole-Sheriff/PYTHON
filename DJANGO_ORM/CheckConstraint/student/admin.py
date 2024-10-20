from django.contrib import admin
from .models import Teacher, Student
from . import forms
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    form = forms.StudentForm

admin.site.register(Teacher, StudentAdmin)
admin.site.register(Student)