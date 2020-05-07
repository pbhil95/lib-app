from django.contrib.auth import logout
from .login import signin


def loggedout(request):
    logout(request)
    return signin(request)
