from django.contrib import admin
from .models import (MaterialDocument, MaterialLink,
                     MaterialVideo, MaterialImage, Material)

# Register your models here.
admin.site.register(Material)
admin.site.register(MaterialDocument)
admin.site.register(MaterialVideo)
admin.site.register(MaterialLink)
admin.site.register(MaterialImage)
