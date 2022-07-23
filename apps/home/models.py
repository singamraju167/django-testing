from email.policy import default
from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# class Job_postings(models.Model):
#     j_id = models.IntegerField(default=" ")
#     main_img = models.ImageField(upload_to='images/', default = " ")
#     title = models.CharField(max_length=30)
#     j_post = models.TextField(default=" ")
    
#     def __str__(self):
#         return self.title

#Newly added tables

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    main_img = models.ImageField(upload_to='images', default = " ")
    description = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[
        ('youtube', '/static/ckeditor/ckeditor_plugins/youtube/', 'plugin.js',)],)
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
