# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):
    def process_registration(self, postData):
        print "inside UserManager"
        # Build a response dict to send back to views
        response = {}
        errors = [] # list of all validation errors. If none => valid registration input

        # checks name that needs to be at least 3 char long. If shorter => generate error
        if len(postData["first_name"]) < 3 or len(postData["last_name"]) < 3:
            # or len(postData["last_name"]) < 3 or len(postData["username"])
            errors.append("Names and Usernames must be at least 3 characters.")

        # Checks if the entered passwords match
        if postData["reg_pw"] != postData["confirm_reg_pw"]:
            errors.append("Entered passwords must match")   
        # Checks for a minimum length of entered password:
        if len(postData['reg_pw']) < 8:
            errors.append("Password must contain at least 3 charcters")
        
        # Check if username is entered & if valid length
        if len(postData["username"]) <3:
            errors.append("Usernames must be at least 3 characters.")
        if len(postData["username"]) < 1:
            print "in username check!!!!!!!!"
            errors.append("Please enter an username")
        # Check if username is already in database w/querys
        check_db_username = User.objects.filter(username=postData['username'])
        if len(check_db_username) > 0:
            errors.append("username is already registered in our database.")
            print "username aaaaaaaaaaaaaaaaaaaa"

        # If errors has a length of 0, the registration submission was valid and successful
        if len(errors) == 0:
            new_pw = bcrypt.hashpw(postData["reg_pw"].encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name=postData["first_name"], last_name=postData["last_name"], username=postData["username"], password=new_pw)
            response["new_user"] = new_user
        # If errors has any length, our submission was invalid, and we need to display errors on HTML
        else:
            response["errors"] = errors
            print response["errors"]

        return response
    
    def process_login(self, postData):
        print "inside process_login in models!!"
        # Build response dict to send back to views
        response = {}
        errors = []

        # Error if no username in login form submission
        if len(postData['username']) == 0:
            errors.append("Please enter an username")
        # Grab user info from database, based on submitted username:
        else: 
            check_user = User.objects.filter(username=postData['username'])
            # if we were returned a list that has a matched User obj from the submitted username:
            if len(check_user):
                # 1.) use bycrypt's checkpw method to compare submitted pw to pw in database
                new_pw = bcrypt.checkpw(postData['login_pw'].encode(), check_user[0].password.encode())
                if new_pw:
                    response["logged_in_user"] = check_user
                # if login pw doesn't match db pw:
                else: 
                    errors.append("Incorrect password")
            # If no matching username from the form submission
            else:
                errors.append("Username is not registered in our database.")
        
        response['errors'] = errors
        return response


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()