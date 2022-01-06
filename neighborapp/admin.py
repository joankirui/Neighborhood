from django.contrib import admin

from neighborapp.models import Neighborhood, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighborhood)