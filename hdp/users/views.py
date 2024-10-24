from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser


def home(request):
    return render(request, 'html/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('login_success')  # Redirect to success page
        else:
            # Invalid credentials, show error message
            return render(request, 'html/login.html', {'error': 'Invalid username or password'})

    return render(request, 'html/login.html')


# Create your views here.


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        hospital_name = request.POST['hospital_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validation: Check if passwords match
        if password != confirm_password:
            return render(request, 'html/register.html', {'error': 'Passwords do not match'})

        # Check if username or email already exists
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'html/register.html', {'error': 'Username already taken'})

        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'html/register.html', {'error': 'Email already registered'})

        # Create new user
        user = CustomUser.objects.create(
            username=username,
            hospital_name=hospital_name,
            email=email,
            phone_number=phone_number,
            password=make_password(password)  # Hash the password before saving
        )
        user.save()
        return redirect('registration_success')  
        # Log the user in after registration
        login(request, user)
        return redirect('home')  # Redirect to home page after successful registration

    return render(request, 'html/register.html')

def registration_success_view(request):
    return render(request, 'html/registration_success.html')

def login_success_view(request):
    return render(request, 'html/login_success.html')
