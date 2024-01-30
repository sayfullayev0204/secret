from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            messages.success(request, 'Muvaffaqiyatli ro\'yxatdan o\'tdingiz!')
            login(request, user)
            return redirect('/')  # Change 'post/' to the appropriate URL

    return render(request, 'registration/register.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('/')  # Change 'home/' to the appropriate URL for your home page
