from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm, UserForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.context_processors import csrf
from django.db import transaction

def index(request):
    """A view the returns the index page"""
    return (request, 'index.html')

def user_login(request):
    """View that returns the login form"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                        password=request.POST['password'])
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Your username or password is incorrect")
    else:
        user_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': user_form})

@login_required
def user_logout(request):
    auth.logout(request)
    messages.success(request, "You have been successfully logged out. See you soon!")
    return redirect(reverse('index'))

def user_registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method=="POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'register.html', {"registration_form": registration_form})

@login_required
def view_profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'profile.html', {'user': user})
    else:
        return redirect(reverse('user_login'))

@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        print(request.POST)
        user_form = UserForm(request.POST, instance=request.user)
        print(request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Yay! You updated your profile!'))
            return redirect(reverse('view_profile'))
        else:
            messages.error(request, "Yikes couldn't manage that, please correct the errors below")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {"user_form": user_form, "profile_form": profile_form})