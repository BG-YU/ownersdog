from movies.views import DogsListView
from django.urls import path
from .views import DogsListView, DogReg

urlpatterns = [
    path('', DogsListView.as_view()),
    path('/reg', DogReg.as_view())
]
