"""
URL configuration for django_post_formats project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("api/urlencoded/", views.handle_urlencoded, name="handle_urlencoded"),
    path("api/multipart/", views.handle_multipart, name="handle_multipart"),
    path("api/json/", views.handle_json, name="handle_json"),
    path("api/ndjson/", views.handle_ndjson, name="handle_ndjson"),
    path("api/text/", views.handle_text_plain, name="handle_text_plain"),
    path("api/html/", views.handle_html, name="handle_html"),
    path("api/xml/", views.handle_xml, name="handle_xml"),
    path("api/svg/", views.handle_svg, name="handle_svg"),
    path("api/binary/", views.handle_binary, name="handle_binary"),
]
