from django.shortcuts import render
import libapp.models as mymodel
from ..util import disable_link, disable_return_link


def display_issued_book(request):
    if request.user.is_authenticated:
        data = mymodel.Issue.objects.filter(roll=request.user.roll)
        return render(request, "displayissuedbook.html", {'data': data})


def display_returned_book(request):
    if request.user.is_authenticated:
        datax = mymodel.Return.objects.filter(roll=request.user.roll)
        data = disable_return_link(request, datax)
        return render(request, "displayreturnedbook.html", {'data': data})


def bookstore(request):
    datax = mymodel.Libook.objects.all()
    data = disable_link(request, datax)
    return render(request, "bookstore.html", {'data': data})
