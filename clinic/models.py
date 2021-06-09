from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=50)
    text = RichTextField()
    date = models.DateField()
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=False, null=True)
    image_2 = models.ImageField(blank=True, null=True)
    image_3 = models.ImageField(blank=True, null=True)
    image_4 = models.ImageField(blank=True, null=True)
    slug = models.SlugField(blank=False, null=True)

    class Meta:
        verbose_name="Blog"
        verbose_name_plural="Blog"

    def __str__(self):
        return self.title


class Departments(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=False, null=True)
    slug = models.SlugField(blank=False, null=True)
      
    class Meta:
        verbose_name="Departments"
        verbose_name_plural="Departments"

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=False, null=True)
    
    class Meta:
        verbose_name="Comments"
        verbose_name_plural="Comments"

    def __str__(self):
        return self.post.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name="Contact"
        verbose_name_plural="Contact"

    def __str__(self):
        return self.post.title


class Professional(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = RichTextField()
    photo = models.ImageField()

    slug = models.SlugField(blank=False, null=True)

    class Meta:
        verbose_name="Professional"
        verbose_name_plural="Professional"


    def __str__(self):
        return self.name

class Career(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    open = models.BooleanField(default=False, blank=True, null=False)
    text = RichTextField()
    slug = models.SlugField(blank=False, null=True)

    class Meta:
        verbose_name="Professional"
        verbose_name_plural="Professional"


    def __str__(self):
        return self.name
