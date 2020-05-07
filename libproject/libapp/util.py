# pylint:disable=E1101
from random import randint
from django.shortcuts import render
from libapp.models import Issue
from .forms import LoginForm


def create_newid(bids, x):
    if x:
        col_list = []
        bid_list = Issue.objects.filter(bname=x.bname).values_list("bid")
        for count, ele in enumerate(bid_list):
            bookid = (bid_list[count][0])
            idx = " "
            for j in bookid:
                if j.isdigit():
                    idx = idx+j
            col_list.append(int(idx))
        newid = randint(1, x.bno)
        while newid in col_list:
            newid = randint(1, x.bno)
        newbookid = bids+str(newid)
        return newbookid
    else:
        return False


def disable_link(request, data):
    search_data = {}
    i = 0
    book_list = []
    book = Issue.objects.filter(roll=request.user.roll).values_list('bname')
    for count, ele in enumerate(book):
        book_list.append(book[count][0])
    for row in data:
        sdata = {
            "bname": row.bname,
            "bid": row.bid,
            "bno": row.bno,
            "avlbook": row.avlbook,
        }
        i = i+1
        if row.bname in book_list:
            sdata["action"] = "disable"
        else:
            sdata["action"] = "enable"
        search_data[str(i)] = sdata
    return search_data


def disable_return_link(request, data):
    search_data = {}
    i = 0
    book_list = []
    book = Issue.objects.filter(roll=request.user.roll).values_list('bname')
    for count, ele in enumerate(book):
        book_list.append(book[count][0])
    for row in data:
        sdata = {
            "bname": row.bname,
            "bid": row.bid,
            "returndate": row.returndate,
        }
        i = i+1
        if row.bname in book_list:
            sdata["action"] = "disable"
        else:
            sdata["action"] = "enable"
        search_data[str(i)] = sdata
    return search_data


def check_admin(func):
    def helper(request):
        if request.user.is_authenticated and request.user.is_admin == 1:
            return func(request)
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    return helper


def check_auth(func):
    def helper(request, roll):
        roll = request.user.roll
        return func(request, roll)
    return helper
