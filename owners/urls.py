from django.urls import path
from .views import OwnersListView, OwnersDogList, OwnersReg

urlpatterns = [
    path('', OwnersListView.as_view()),
    path('/ownersdoglist', OwnersDogList.as_view()),
    path('/reg', OwnersReg.as_view())
]