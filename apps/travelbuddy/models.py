# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User
import datetime 

class TripManager(models.Manager):
    def add_trip(self, postData):
        print "inside TripManager!"
        # Build a response dict to send back to views
        response = {}
        errors = []

        # no empty entries
        '''
        if (len(postData['destination']) < 1) or (len(postData['description']) < 1) or (len(postData['from_date']) < 1) or (len(postData['to_date']) < 1):
            print "if check!"
            errors.append("All fields are required. Please ensure you've filled all entries")
            print errors
        '''
            # add Trip
        new_trip = Trip.objects.create(destination=postData["destination"], description=postData["description"], travel_from_date=postData["from_date"], travel_to_date=postData["to_date"])
        print new_trip
        return response
          
# class TravelManager(models.Manager):

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_from_date = models.DateTimeField(default=datetime.datetime.now())
    travel_to_date = models.DateTimeField(default=datetime.datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()

class TravelPlan(models.Model):
    trip = models.ForeignKey(Trip, related_name="travel_plans")
    user = models.ForeignKey(User, related_name="travel_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = TravelPlan()

