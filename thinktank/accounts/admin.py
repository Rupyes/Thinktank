from django.contrib import admin
from .models import Student, Faculty, MyUser, College, University, Department

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(College)
admin.site.register(University)
admin.site.register(Department)
