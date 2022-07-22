# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job_postings(models.Model):
    j_id = models.IntegerField()
    main_img = models.ImageField(upload_to='images/', default = " ")
    title = models.CharField(max_length=30)
    j_post = models.TextField()
    
    def __str__(self):
        return self.title

