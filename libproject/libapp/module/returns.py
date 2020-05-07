from django.shortcuts import render
from django.contrib import messages
import libapp.models as mymodel
from ..forms import SearchBookForm, ReturnBookForm, LoginForm
from .profile import home


def returns(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReturnBookForm(request.POST)
            if form.is_valid():
                bookid = form.cleaned_data["bid"]
                form_user = form.cleaned_data["roll"]
                current_user = request.user.roll
                y = mymodel.Issue.objects.filter(bid=bookid).first()
                x = mymodel.Libook.objects.filter(bname=y.bname).first()
                if current_user == form_user.roll:
                    x.avlbook = x.avlbook+1
                    x.save(update_fields=["avlbook"])
                    y.delete()
                    form.save()
                    messages.success(request, "Book returned sucessfully")
                    return home(request)
            return render(request, "return.html", {'form': form})
    messages.success(request, "please login first")
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def return_book(request, **bid):
    if not bid:
        if request.method == "POST":
            form = SearchBookForm(request.POST)
            if form.is_valid():
                bookid = form.cleaned_data.get("bid")
                return return_book_now(request, bookid)
        else:
            form = SearchBookForm()
        return render(request, "returnbook.html", {"form": form})
    else:
        return return_book_now(request, bid["bid"])


def return_book_now(request, bookid):
    x = mymodel.Issue.objects.filter(
        bid=bookid, roll=request.user.roll).first()
    if x:
        form = ReturnBookForm(instance=x)
        return render(request, 'return.html', {'form': form})
    else:
        y = mymodel.Issue.objects.filter(
            bname=bookid, roll=request.user.roll).first()
        form = ReturnBookForm(instance=y)
        return render(request, 'return.html', {'form': form})
