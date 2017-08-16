from django.contrib import admin
from .models import Header , About , Service , Parallax
# Register your models here.

myModels = [Header ,About , Service , Parallax]  # iterable list



admin.site.register(myModels)