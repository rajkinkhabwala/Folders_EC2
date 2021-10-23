from django.urls import path
from helloworld.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]
