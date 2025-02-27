from django.shortcuts import render
from Login_app import forms

# Create your views here.
def index(request):
    dict = {
        'headings':'successfully worked!'
    }
    return render(request, 'login_app/index.html', context=dict)

def register(request):
    registered = False
    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        user_info_form = forms.UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            print(request.FILES)
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
    dict = {}

    return render(request, 'login_app/Log_in.html', context=dict)