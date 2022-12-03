from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from datetime import datetime
from .models import Contact


# Create your views here.
from bidbro.models import product


def index(request):
     return render(request, 'index.html')

def participate(request):
     return render(request, "participate.html")

def categories(request):
     prod = product.objects.all()
     return render(request, "categories.html", {'prod': prod})

def createbid(request):
     return render(request,"creating_bid.html")

def contact(request):
    if request.method == "POST":
        contact_name = request.POST('contact_name')
        contact_email = request.POST('contact_email')
        contact_phone = request.POST('contact_phone')
        contact_comment = request.POST('contact_comment')
        contact = Contact(contact_name=contact_name, contact_email=contact_email,
                          contact_phone=contact_phone, contact_comment=contact_comment, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        print("Information Recieved")
        messages.info(request, 'Information Recieved')
    return render(request, '/')





