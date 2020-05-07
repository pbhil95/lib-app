from django.shortcuts import render
from django.contrib import messages
import libapp.models as mymodel
from ..forms import IssueBookForm, SearchBookForm, LoginForm
from ..util import create_newid
from .profile import home


def issue(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = IssueBookForm(request.POST)
            if form.is_valid():
                bookname = form.cleaned_data["bname"]
                form_user = form.cleaned_data["roll"]
                current_user = request.user.roll
                x = mymodel.Libook.objects.filter(bname=bookname).first()
                if current_user == form_user.roll:
                    x.avlbook = x.avlbook-1
                    x.save(update_fields=["avlbook"])
                    form.save()
                    messages.success(request, "Book issued sucessfully")
                    return home(request)
            return render(request, "issue.html", {'form': form})
    messages.success(request, "please login first")
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def issue_book(request, **bid):
    if not bid:
        if request.method == "POST":
            form = SearchBookForm(request.POST)
            if form.is_valid():
                bookid = form.cleaned_data.get("bid")
                return issue_book_now(request, bookid)
        else:
            form = SearchBookForm()
        return render(request, "issuebook.html", {"form": form})
    else:
        return issue_book_now(request, bid["bid"])


def issue_book_now(request, bookid):
    x = mymodel.Libook.objects.filter(bid=bookid).first()
    if x:
        idn = create_newid(bookid, x)
        bname = x.bname
    else:
        y = mymodel.Libook.objects.filter(bname=bookid).first()
        bookid = y.bid
        bname = y.bname
        idn = create_newid(bookid, y)
    if idn:
        data = {
            "roll": request.user.roll,
            "bid": idn,
            "bname": bname
        }
        form = IssueBookForm(initial=data)
        return render(request, 'issue.html', {'form': form})
