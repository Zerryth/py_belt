# app level urls - TRAVELBUDDY
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'/process_adding_trip', views.process_adding_trip),
    url(r'/add', views.show_add_trip),
    url(r'^', views.dashboard)
]