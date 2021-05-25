from django.urls import path
from .views import OwnersListView, OwnersReg

urlpatterns = [
    path('', OwnersListView.as_view()),
    path('/reg', OwnersReg.as_view())
]