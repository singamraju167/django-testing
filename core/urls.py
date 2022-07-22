# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include  # add this

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line 
    path("", include("apps.home.urls"))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
