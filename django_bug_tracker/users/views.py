from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    # Check the validity of the entered items
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been create! You may now log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
               
    return render(request, 'users/register.html', {'form': form})
