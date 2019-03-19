from django.contrib import admin
from .models import (Software, Configuration, WorkingProject, Technology,)

# Register your models here.
admin.site.register(Software)
admin.site.register(Configuration)
admin.site.register(WorkingProject)
admin.site.register(Technology)
