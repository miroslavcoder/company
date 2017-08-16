from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.

class Header(models.Model):
    title = models.CharField( max_length=250)
    description = models.CharField( max_length=250)
    cover_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField( auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

#About
class About(models.Model):
     about_title = models.CharField( max_length=250)
     about_description = models.CharField( max_length=250)
     about_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
     experience_year  = models.CharField( max_length=50)
     experience  = models.CharField( max_length=50)
     about_title2 = models.CharField( max_length=250)
     about_description2 = models.CharField( max_length=250)
     about_photo2 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
     
     created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
     updated_at = models.DateTimeField( auto_now=False, auto_now_add=True)
     
     def __str__(self):
        return self.title