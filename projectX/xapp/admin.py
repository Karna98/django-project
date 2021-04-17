from django.contrib import admin

# Register your models here.
from .models import Topic, Opinion

# Registering Topic and Opinion Model
admin.site.register([Topic, Opinion])