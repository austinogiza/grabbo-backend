from django.db import models
from django.db.models.fields import related
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True,blank=False, null=True)


    class Meta:
        verbose_name="Contact"
        verbose_name_plural="Contact"

    def __str__(self):
        return self.name
