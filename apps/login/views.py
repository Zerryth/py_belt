from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User

def login_register(request):
    return render(request, 'login/login_registration.html')

def show_user_profile(request, user_id):
    print user_id

    return render(request, 'login/user_profile.html')

def process_registration(request):
    registration_results = User.objects.process_registration(request.POST)
    # print registration_results
    print "inside registration process"
    if "new_user" in registration_results:
        request.session['first_name'] = registration_results['new_user'].first_name
        request.session['last_name'] = registration_results['new_user'].first_name
        return redirect('/travels')
    else:
        # print registration_results["errors"]
        for message in registration_results['errors']:
            print message
            messages.error(request, message)
        return redirect('/')

def process_login(request):
    login_results = User.objects.process_login(request.POST)
    print login_results
    print "*****inside login_process in views****"

    if "logged_in_user" in login_results:
        print "***********successful login!******"
        request.session['user_id'] = login_results['logged_in_user'][0].id
        request.session['first_name'] = login_results['logged_in_user'][0].first_name
        request.session.modified = True
        return redirect('/travels')
    # If our results contains errors, we grab all errors from response and store in messages object. Errors, created from models, is a list
    else:
        print login_results["errors"]
        for message in login_results['errors']:
            messages.error(request, message)
        return redirect('/')

def logout(request):
    request.session.clear()
    print "logged out!!"
    return redirect('/')