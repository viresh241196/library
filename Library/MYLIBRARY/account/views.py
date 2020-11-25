from django.contrib import auth, messages
from django.shortcuts import render, redirect

from library.models import Profile
from .forms import UserAdminCreationForm, LoginForm, ProfileRegister
from .models import CustomUser


def register(req):
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        profile_form = ProfileRegister(req.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user_info = user
            new_profile.save()
            pk = new_profile.user_info
            Profile.objects.filter(user_info=pk).update(email_id=user.email, name=user.username)
            return redirect('home')
    else:
        form = UserAdminCreationForm()
        profile_form = ProfileRegister()
    return render(req, 'register.html', {'form': form, 'profile_form': profile_form})


def about(request):
    if request.method == 'POST':

        profile_form = ProfileRegister(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = ProfileRegister()
    return render(request, 'about.html', {'profile_form': profile_form})


# def about(request):
#     return render(request, 'about.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        login_form = LoginForm()
    return render(request, 'account/login.html', {'login_form': login_form})


def logout(request):
    auth.logout(request)
    return redirect('home')
