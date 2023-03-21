from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
# import mimetypes
# import os
from django.http import StreamingHttpResponse

from django.core.mail import send_mail
from django.conf import settings

# un= portfolio
# p= 123

# Create your views here.
def index(request):

    return render(request, 'index.html')


def contact(request):

        if request.method == 'POST':
            name = request.POST.get('name')
            email = (request.POST.get('email'))
            phone = (request.POST.get('phone'))
            message = request.POST.get('message')
            
            if len(name)<2 or len(email)<3 or len(phone)<10 or len(message)<2:
                 messages.error(request,'Please fill the form correctly')
            else:
                cont = Contact(name=name, phone=phone, email=email, message=message)
                cont.save()
                messages.success(request,'Your message has been submitted') 

            subject = 'about registration'
            message= f'hi {name}, you has been successfull '
            email_from = 'palshobhit318@gmail.com'
            rec_list = [ email, 'palshobhit318@gmail.com' ]
            send_mail(subject,message, email_from, rec_list)
        return render(request,'contact.html')
    
    


