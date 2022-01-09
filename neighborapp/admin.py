from django.contrib import admin

from neighborapp.models import Neighborhood, Profile,Post,Business

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(Post)
admin.site.register(Business)
