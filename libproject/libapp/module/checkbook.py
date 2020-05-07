import libapp.models as mymodel
from . import issue
from . import returns


def check_book(request, **bid):
    if bid:
        check = mymodel.Issue.objects.filter(
            bname=bid["bid"], roll=request.user.roll)
        if check:
            return returns.return_book_now(request, bid["bid"])
    return issue.issue_book_now(request, bid["bid"])
