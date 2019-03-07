from django.contrib import admin
from .models import Event, EventPhoto, EventVideo
# Register your models here.
admin.site.register(Event)
admin.site.register(EventPhoto)
admin.site.register(EventVideo)
