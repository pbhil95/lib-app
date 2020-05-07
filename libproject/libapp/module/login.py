from django.shortcuts import render
from django.contrib.auth import authenticate, login
from ..forms import LoginForm
from .profile import home


def signin(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            roll = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(roll=roll, password=raw_password)
            if user.is_authenticated:
                login(request, user)
                return home(request)
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
