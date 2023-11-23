from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home-url')
    else:
        form = RegistrationForm()

        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ". You have created an account successfully")
                return redirect('login-url')

        return render(request, 'auth/register.html', context={"form": form})


def store(request):
    if request.user.is_authenticated:
        return redirect('home-url')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, ". You have successfully logged in")
                return redirect('home-url')
            else:
                messages.info(request, "Email or password is incorrect")

        return render(request, 'auth/login.html')


def getout(request):
    logout(request)
    messages.success(request, "You have successfully logged out. Login again?")
    return redirect('login-url')
