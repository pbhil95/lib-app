from django.urls import path
from .module.adminadd import (activate, admin_pannel, make_admin,
                              profile_verify, rejectprofile, verify,
                              viewprofile)
from .module.adminremove import refute, remove_admin, remove_admin_pannel, deactivate
from .module.display import (bookstore, display_issued_book,
                             display_returned_book)
from .module.issue import issue, issue_book
from .module.login import signin
from .module.logout import loggedout
from .module.profile import home, profile
from .module.returns import return_book, returns
from .module.search import searchbook, searchuser
from .module.signup import signup
from .module.checkbook import check_book

urlpatterns = [
    path("", signin),
    path('signup/', signup),
    path('signin/', signin),
    path('logout/', loggedout),
    path('profile/', profile),
    path('issue/', issue),
    path('return/', returns),
    path('issuebook/<str:bid>/', issue_book),
    path('returnbook/<str:bid>/', return_book),
    path('checkbook/<str:bid>/', check_book),
    path('returnbook/', return_book),
    path('issuebook/', issue_book),
    path('displayissuedbook/', display_issued_book),
    path('displayreturnedbook/', display_returned_book),
    path('home/', home),
    path('bookstore/', bookstore),
    path('searchbook/', searchbook),
    path('adminpannel/', admin_pannel),
    path('removeadminpannel/', remove_admin_pannel),
    path('verify/<int:roll>/', verify),
    path('activate/<int:roll>/', activate),
    path('makeadmin/<int:roll>/', make_admin),
    path('refute/<int:roll>/', refute),
    path('deactivate/<int:roll>/', deactivate),
    path('removeadmin/<int:roll>/', remove_admin),
    path('profileverify/<int:roll>/', profile_verify),
    path('rejectprofile/<int:roll>/', rejectprofile),
    path('viewprofile/', viewprofile),
    path('searchuser/', searchuser),
]
