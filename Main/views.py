from django.shortcuts import render
from Main.models import *


#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.hashers import check_password,make_password
# from json import json_util
#from django.core.mail import send_mail

def Main(request):
    events=Events.objects.all()
    return render(request, 'Main.html', locals())