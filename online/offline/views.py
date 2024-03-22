from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import vote
from django.db.models import Q


# Create your views here.
def anil(request):
    # d=vote.objects.all()
    return render(request,"first.html")
login_required(login_url='signin')
def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,"You are successfully Logged!")
            return redirect("display")
        else:
            messages.info(request,"Username or Password incorrect !")
            return redirect("signin")
    return render(request,"signin.html")


def signup(request):
    if request.method=="POST":
        
        username=request.POST.get('username')
        email=request.POST.get('email')
        vote_id=request.POST.get('vote_id')
        age=request.POST.get('age')
        mandal=request.POST.get('mandal')
        distic=request.POST.get('distic')
        state=request.POST.get('state')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            user=User.objects.create_user(username=username,password=password,email=email,)
            vote.objects.create(vote_id=vote_id,age=age,mandal=mandal,distic=distic,state=state,uid_id=user.id)
            messages.info(request,"Successfully Register Logged Now!")
            return redirect("display")
        else:
            messages.info(request,"Password Do Not Match Please Try Again! ")
            return redirect("signup")
    return render(request,"signup.html")


def display(request):
    if request.method=="POST":
        if request.POST.get('display'):
            d=vote.objects.all()
            return render(request,"second.html",{"table":d})
        messages.info(request,"Display details successfully")
    return render(request,"second.html")

def search(request):
    if request.method=="POST":
        search=request.POST.get('search')
        distic = vote.objects.filter(Q(mandal=search)|Q(distic=search))
        print(distic)
        print(request.user.username)
    return render(request,"second.html",{"table":distic})


def contact(request):
    d=vote.objects.all()
    return render(request,"contact.html",{"table":d})

def fool(request):
    return render(request,"fool.html")
def delete(request, id):
     vote.objects.get(id = id).delete()
     return redirect('display')
def update(request,id):
    item=vote.objects.get(id = id)
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        vote_id=request.POST.get('vote_id')
        age=request.POST.get('age')
        mandal=request.POST.get('mandal')
        distic=request.POST.get('distic')
        state=request.POST.get('state')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        item.vote_id=username
        item.vote_id=email
        item.vote_id=vote_id
        item.vote_id=age
        item.vote_id=mandal
        item.vote_id=distic
        item.vote_id=state
        item.vote_id=password
        item.vote_id=confirm_password
        item.save()
        # vote.objects.filter(id=id).update(vote_id=vote_id,age=age,mandal=mandal,distic=distic,state=state)
        return redirect('display')
    return render(request,"second.html")
def signout(request):
    messages.info(request,"Successfully Log Out")
    logout(request)
    return redirect("chinni")
def chinni(request):
    return render(request,"own.html")