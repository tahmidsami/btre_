from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        # Login User
        messages.error(request, 'Tessting error message')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check for password match
        if password == password2:
            # Check username
            if User.objects.filter(email = email).exists():
                messages.error(request, 'Email already used!')
                return redirect('register')
            else:
                if User.objects.filter(username = username).exists():
                    messages.error(request, 'Username already taken')
                    return redirect('register')
                else:
                    # Create user
                    user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                    user.save()
                    messages.success(request, 'Registration Successfull. Please log in.')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('index')


