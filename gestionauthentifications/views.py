from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('gestionarticles:articles'))
    return render(request, 'gestionauthentifications/login.html', {})

def logout_user(request):
    logout(request)
    return render(request, 'gestionauthentifications/login.html', {})
