# app level urls - login

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/(?P<user_id>\d+)', views.show_user_profile),
    url(r'^process_registration$', views.process_registration),
    url(r'^process_login$', views.process_login),
    url(r'^logout$', views.logout),
    url(r'^$', views.login_register)
]