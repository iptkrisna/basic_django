from django.contrib import admin
from . import models

admin.site.site_header = 'STEMian'
admin.site.register(models.Major)
admin.site.register(models.Student)
