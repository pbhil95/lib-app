from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
import libapp.models as mymodel
from ..forms import UpdateProfileForm, LoginForm


def profile(request):
    if request.user.is_authenticated:
        x = mymodel.Profile.objects.filter(roll=request.user.roll).first()
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, request.FILES, instance=x)
            if form.is_valid():
                form.save()
                filed_flag = check_profile(request)
                if filed_flag != 0:
                    mymodel.MyUser.objects.filter(
                        roll=request.user.roll).update(is_verified=filed_flag)
                    request.user.refresh_from_db()
                messages.success(request, "Profile updated sucessfully")
                # return render(request,"base.html")
                return home(request)
            else:
                return render(request, 'updateprofile.html', {'form': form})
        else:
            form = UpdateProfileForm(instance=x)
            return render(request, 'updateprofile.html', {'form': form})
    else:
        messages.success(request, "please login first")
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def check_profile(request):
    check = 0
    c_fname = Q(fname__isnull=True)
    c_lname = Q(lname__isnull=True)
    c_img = Q(img__isnull=True)
    c_clss = Q(clss__isnull=True)
    c_gender = Q(gender__isnull=True)
    c_section = Q(section__isnull=True)
    c_dob = Q(dob__isnull=True)
    profile_flag_check = mymodel.Profile.objects.filter(roll=request.user.roll).filter(
        c_fname | c_lname | c_clss | c_gender | c_section | c_dob | c_img)
    if not profile_flag_check:
        check = 1
    return check


def home(request):
    check_user_status = mymodel.MyUser.objects.filter(
        roll=request.user.roll).first().is_verified
    if check_user_status == 2:
        form = {}
        last_issuebook = "No book issued"
        last_returnbook = "No book returned"
        try:
            fname = mymodel.Profile.objects.filter(
                roll=request.user.roll).first().fname
            if fname == "":
                fname = "Not set"
                messages.warning(request, "please update your profile first !")
            img = mymodel.Profile.objects.filter(
                roll=request.user.roll).first().img
            issue_count = mymodel.Issue.objects.filter(
                roll=request.user.roll).count()
            if mymodel.Issue.objects.filter(roll=request.user.roll).exists():
                last_issuebook = mymodel.Issue.objects.filter(
                    roll=request.user.roll).latest('issuedate').bname
            if mymodel.Return.objects.filter(roll=request.user.roll).exists():
                last_returnbook = mymodel.Return.objects.filter(
                    roll=request.user.roll).latest('returndate').bname
            # print(fname,issue_count,last_issuebook,last_returnbook)
            form = {
                'fname': fname,
                'img': img,
                'issue_count': issue_count,
                'last_issuebook': last_issuebook,
                'last_returnbook': last_returnbook,
            }
            return render(request, "profile.html", {'form': form})
        except Exception as e:
            return render(request, "profile.html", {'form': form})
    return render(request, "base.html")
