from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=User.objects.create_user(username=username, 
                                      email=username, 
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, 'auth/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        authenticated_user=authenticate(request,username=username,password=password)
        if authenticated_user is not None:
            login(request,authenticated_user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'auth/login.html')