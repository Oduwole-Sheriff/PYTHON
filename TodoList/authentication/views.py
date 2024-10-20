from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username}! , you can now Login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})

