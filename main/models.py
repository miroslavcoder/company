from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.

class Header(models.Model):
    title = models.CharField(, max_length=250)
    description = models.CharField(, max_length=250)
    cover_photo = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(, auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(, auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title