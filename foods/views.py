# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,reverse,get_object_or_404
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ReceipeForm

def registration(request):
    if request.method=="POST":
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            password=request.POST['password']
            )
        return HttpResponseRedirect(reverse('foods:login_view'))
    return render(request,"registration.html")

def login_view(request):
    if request.method=="POST":
       user= authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
       if user is not None:
           login(request,user)
           return HttpResponseRedirect(reverse("foods:index"))
       else:
          # return HttpResponse("INAVALID credientials")
           return HttpResponseRedirect(reverse("foods:registration"))
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("foods:index"))
        return render(request, "login.html")

@login_required(login_url='/foods/login_view/')
def index(request):
    print request.user
    receipe_list=Receipe.objects.all()
    return render(request,"index.html",{"receipe_list":receipe_list})

@login_required(login_url='/foods/login_view/')
def create_receipe(request):
    if request.method=="POST":
        Receipe.objects.create(
            receipe_name=request.POST["receipe_name"],
            ingredients=request.POST['ingredients'],
            process=request.POST['process'],
            image=request.FILES['image'],
            user=request.POST['user']
        )
        return HttpResponseRedirect(reverse('foods:index'))
    return render(request,"create.html")

@login_required(login_url='/foods/login_view/')
def details(request,receipe_id):
    receipe=get_object_or_404(Receipe,id=receipe_id)
    return render(request,"details.html",{"receipe":receipe})

@login_required(login_url='/foods/login_view/')
def delete(request,receipe_id):
    receipe=get_object_or_404(Receipe,id=receipe_id)
    receipe.delete()
    return HttpResponseRedirect(reverse("foods:index"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("foods:login_view"))

def createform(request):
    if request.method=='POST':
        form=ReceipeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('foods:index'))
        else:
            form=ReceipeForm()
            return render(request,"createform.html", {'form':form})
