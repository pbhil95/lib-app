from django.shortcuts import render
from django.db.models import Q
import libapp.models as mymodel
from ..util import disable_link
from django.http.response import HttpResponse, JsonResponse


def searchbook(request):
    bookref = request.GET.get("bookref")
    if bookref:
        q1 = Q(bname__icontains=bookref)
        q2 = Q(bid__icontains=bookref)
        data = mymodel.Libook.objects.filter(q1 | q2)
        #search_data = disable_link(request, data)
        book = {}
        i = 0
        for row in data:
            book[i] = row.bname
            i = i + 1
        return JsonResponse(book)
    # return render(request, "searchresult.html", {"data": search_data})


def searchuser(request):
    roll = request.POST.get("roll", False)
    if roll:
        rollno = mymodel.MyUser.objects.filter(roll=roll).first()
        if rollno:
            user = {"user": "1"}
            return JsonResponse(user)
        user = {"user": "2"}
    return JsonResponse(user)
