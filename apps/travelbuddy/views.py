# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from time import localtime, strftime

def dashboard(request):
    user_trips = Trip.objects.filter(id=request.session['user_id'])
    all_travels = TravelPlan.objects.all()
    first_name = request.session['first_name']
    context = {
        "first_name": first_name,
        "user_trips": user_trips
        }
    
    print context
    print context
    return render(request, 'travelbuddy/dashboard.html', context)

def show_add_trip(request):
    return render(request, 'travelbuddy/add_trip.html')

def process_adding_trip(request):
    
    print "inside process adding trip"
    user_id = request.session["id"]
    print user_id
    results_add_trip = Trip.objects.add_trip(request.POST)

    return redirect('/travels')