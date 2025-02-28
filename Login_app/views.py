from django.shortcuts import render
from Login_app import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from Login_app import models


# Create your views here.
def index(request):
    dict = {}
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = models.UserInfo.objects.filter(user__pk=user_id).first()
        dict = {
            'user_basic_info':user_basic_info,
            'user_more_info':user_more_info,

        }
    return render(request, 'login_app/index.html', context=dict)

def register(request):
    registered = False
    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        user_info_form = forms.UserInfoForm(data=request.POST, files=request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user


            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()
            registered = True

    else:
        user_form = forms.UserForm()
        user_info_form = forms.UserInfoForm()
    dict = {
        'registered':registered,
        'user_form':user_form,
        'user_info_form': user_info_form,
    }

    return render(request, 'login_app/register.html', context=dict)


def logIn(request):
    return render(request, 'login_app/Log_in.html', context={})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Login_app:index'))
            else:
                return HttpResponse ("the user is not active")
        else:
            return HttpResponse("The information is not valid")

    else:
        return HttpResponseRedirect(reverse('login_app/Log_in.html'))

@login_required
def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:index'))
