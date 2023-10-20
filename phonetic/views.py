from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('phonetic:index')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'auth/login.html', {'error_message': error_message})
    else:
        return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('phonetic:index')
            except:
                error_message = 'Error creating account'
                return render(request, 'auth/register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'auth/register.html', {'error_message': error_message})
    return render(request, 'auth/register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def index(request):
    return render(request, 'phonetic/index.html')
def get_started(request):
    return render(request, 'get_started/index.html')