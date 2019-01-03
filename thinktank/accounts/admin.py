from django.contrib import admin
from .models import Student, Faculty, MyUser

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Student)
admin.site.register(Faculty)