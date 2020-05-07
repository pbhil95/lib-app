from django.contrib import messages
from django.shortcuts import render
import libapp.models as mymodel
from ..util import check_admin


@check_admin
def remove_admin_pannel(request):
    data = mymodel.MyUser.objects.all()
    return render(request, "removeadminpannel.html", {"data": data})


def refute(request, roll):
    obj = mymodel.MyUser.objects.get(roll=roll)
    mymodel.MyUser.objects.filter(roll=roll).update(is_verified=1)
    obj.refresh_from_db()
    messages.error(request, "User: "+str(roll)+" Refuted Successfullly !")
    return remove_admin_pannel(request)


def deactivate(request, roll):
    obj = mymodel.MyUser.objects.get(roll=roll)
    mymodel.MyUser.objects.filter(roll=roll).update(is_active=0)
    obj.refresh_from_db()
    messages.error(request, "User: "+str(roll)+" Dectivated Successfullly !")
    return remove_admin_pannel(request)


def remove_admin(request, roll):
    obj = mymodel.MyUser.objects.get(roll=roll)
    mymodel.MyUser.objects.filter(roll=roll).update(is_admin=0)
    obj.refresh_from_db()
    messages.error(request, "User: "+str(roll)+" Is Removed From Admin !")
    return remove_admin_pannel(request)
