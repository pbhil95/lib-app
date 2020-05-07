from django.shortcuts import render
from django.contrib import messages
import libapp.models as mymodel
from ..util import check_admin


@check_admin
def admin_pannel(request):
    data = mymodel.MyUser.objects.all()
    return render(request, "adminpannel.html", {"data": data})


def verify(request, roll):
    obj = mymodel.MyUser.objects.get(roll=roll)
    mymodel.MyUser.objects.filter(roll=roll).update(is_verified=2)
    obj.refresh_from_db()
    messages.success(request, "User: "+str(roll)+" Veified Successfullly !")
    return admin_pannel(request)


def activate(request, roll):
    obj = mymodel.MyUser.objects.get(roll=roll)
    mymodel.MyUser.objects.filter(roll=roll).update(is_active=1)
    obj.refresh_from_db()
    messages.success(request, "User: "+str(roll)+" Activated Successfullly !")
    return admin_pannel(request)


def make_admin(request, roll):
    obj = mymodel.MyUser.objects.get(roll=roll)
    mymodel.MyUser.objects.filter(roll=roll).update(is_admin=1)
    obj.refresh_from_db()
    messages.success(request, "User: "+str(roll)+" is Admin Now !")
    return admin_pannel(request)


def profile_verify(request, roll):
    form = mymodel.Profile.objects.filter(roll=roll)
    return render(request, "table.html", {'form': form})


def rejectprofile(request, roll):
    obj = mymodel.MyUser.objects.get(roll=roll)
    mymodel.MyUser.objects.filter(roll=roll).update(is_verified=3)
    obj.refresh_from_db()
    messages.info(request, "User : " + str(roll) +
                  " Profile's Verification Has Been Rejected !")
    return admin_pannel(request)


def viewprofile(request):
    form = mymodel.Profile.objects.filter(roll=request.user.roll)
    return render(request, "viewprofile.html", {'form': form})
