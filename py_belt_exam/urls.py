# MASTER urls
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^travels', include('apps.travelbuddy.urls')),
    url(r'^', include('apps.login.urls')),
    url(r'^admin/', admin.site.urls),
]
