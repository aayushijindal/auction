from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from auction.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from auction.forms import UserProfileForm
from auction.models import Contact   


def home(request):
    return HttpResponse("Hello world! from members")

def register(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return render(request, 'register_user.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return render(request, 'register_user.html')      
            else:
                user = User.objects.create_user(first_name=first_name,email=email,username=username,password=password1)    #to get value
                    #anyvarname = modelname(modelfieldname = value_var_name from def_function)
                user.save()    #to save value to db
                print("user created")  
                return render(request, 'login_user.html') 
        else:
            messages.info(request,'Passwords unmatched')
            return render(request, 'register_user.html')  
    else:          
        return render(request, 'register_user.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    context = {}
    auth_form = AuthenticationForm(request)
    if request.method == "POST":
        auth_form = AuthenticationForm(request, data=request.POST)
        if auth_form.is_valid():
            user = auth_form.get_user()
            if user:
                login(request, user)
                return redirect('home')     
        else:
            context["error_message"] = auth_form.get_invalid_login_error()
    context["auth_form"] = auth_form
    return render(request, 'login_user.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    context = {}
    signup_form = UserCreationForm()
    profile_edit_form = UserProfileForm()
    context["signup_form"] = signup_form
    context["profile_edit_form"] = profile_edit_form

    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        profile_edit_form = UserProfileForm(request.POST)
        context["signup_form"] = signup_form
        context["profile_edit_form"] = profile_edit_form

        if signup_form.is_valid():
            user = signup_form.save()
        else:
            context["error_message"] = signup_form.errors
            return render(request, 'register_user.html', context)
        if profile_edit_form.is_valid():
            userprofile = profile_edit_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')

    return render(request, 'register_user.html', context)

def forgot_password(request):
    return render(request, 'forgot_password.html')

@login_required
def logout_user(request):
    user = request.user
    logout(request)
    return redirect('login')

def faq(request):
    return render(request, 'faq.html')

#khushi contact
def contact(request):
    return render(request, 'home.html')

def save_contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        en=Contact(c_name=name,c_email=email,c_subject=subject,c_message=message)    #to get value
        #anyvarname = modelname(modelfieldname = value_var_name from def_function)
        en.save()    #to save value to db
    return render(request, 'home.html')

#khushi contact


