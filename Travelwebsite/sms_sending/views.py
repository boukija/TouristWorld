from django.shortcuts import render, redirect
from twilio.rest import Client
from django.http import HttpResponse
from django.contrib import messages


def sending_details(request):
    try:
        account_sid = 'AC828dbef1042ff22b9127bdf30212da88'
        auth_token = '10c727098f09d4b1d265e5bf1be233d4'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                     body="Contact Us Fast For Discounts Contact No: 9713725360, Mayank",
                     from_='+17177272675',
                     to='+919713725360'
                 )
 
        print(message.sid)
        messages.info(request, "Soon YOU Get Details 🥳")
        return redirect("/")
    except Exception as e:
        messages.info(request, "Hmm🤔, Seems Like There is No Internet! ")
        return redirect("/")

