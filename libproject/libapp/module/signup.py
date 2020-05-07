from django.shortcuts import render
from django.contrib import messages
from ..forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Sucessfully registered please login now")
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
