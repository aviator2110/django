from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render, redirect

from accounts.forms import LoginForm, RegisterForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['username_or_email'].strip()
            password = form.cleaned_data['password']

            user = authenticate(request, username=identifier, password=password)
            if user is None:
                User = get_user_model()
                try:
                    candidate = User.objects.get(email=identifier)
                except User.DoesNotExist:
                    candidate = None

                if candidate is not None:
                    user = authenticate(
                        request,
                        username=candidate.username,
                        password=password
                    )
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('accounts:dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('accounts:dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


def logout_view(request):
    return render(request, 'accounts/logout_confirm.html')


def register_success(request):
    return render(request, 'accounts/register_success.html')


def logout_confirm(request):
    return render(request, 'accounts/logout_confirm.html')