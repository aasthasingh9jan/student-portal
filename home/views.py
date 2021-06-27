
from django import forms
from django.http.request import HttpHeaders
from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from .forms import ContactForm, RegisterForm
from django.contrib import messages 
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=='POST':
        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # phone=request.POST.get('phone')
        # msg=request.POST.get('msg')
        # rating=request.POST.get('rating')
        # contact=Contact(name=name,email=email,phone=phone,msg=msg,rating=rating,date=datetime.today())
        # contact.save()
        form = ContactForm(request.POST)
        if request.user.is_authenticated:
            print(request.user,request.user.is_authenticated)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Message has sent.')
                return redirect('/contact')
            ctx = {'contact_form':form}
            return render(request,'contact.html',ctx)
        else:
            messages.error(request,'you are not logged in. Please login and try again')
            ctx = {'contact_form':form}
            return render(request,'contact.html',ctx)
    ctx = {'contact_form':ContactForm}
    return render(request,'contact.html',ctx)

def review(request):
    contacts=Contact.objects.all()
    context={'feeds':contacts}
    return render(request,'review.html',context)

def quora(request):
    return HttpResponse('quora page')

def pyq(request):
    return HttpResponse('pyq page')

def register(request):
    #username=request.get.POST('username')
    #email=request.get.POST('email')
    #password1=request.get.POST('password1')
    #password2=request.get.POST('password2')
    #user=User(username=username,email=email,password1=password1)

    if request.method=='POST':
        rform=RegisterForm(request.POST)
        if rform.is_valid():
            rform.save()
            messages.success(request,'you are successfully registered.')
            return redirect('/login')
        rctx = {'register_form':rform}
        return render(request,'register.html',rctx)
    rctx = {'register_form':RegisterForm()}
    # print(rctx['register_form'])
    return render(request,'register.html',rctx)
