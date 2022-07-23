from multiprocessing import context
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *

from django.shortcuts import get_object_or_404, render
def index(request):
    postings = Post.objects.order_by('publish_date')
    context = {'segment': 'index', 
                'postings': postings
              }
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def blog(request, slug):
    objects = Post.objects.get(slug=slug)
    print(objects.main_img)
    html_template = loader.get_template('home/slug.html')
    print("Blog is running!!!")
    context = {'objects':objects, 'slug': slug}
    return HttpResponse(html_template.render(context, request))


def testing(request):
    postings = Post.objects.order_by('publish_date')
    template = loader.get_template('home/test.html')
    context = {
        'postings': postings
    }
    return HttpResponse(template.render(context, request))

