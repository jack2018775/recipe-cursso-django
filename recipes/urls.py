from django.urls import path
from django.http import HttpResponse
from .views import *

urlpatterns = [
    path('', home ), #Home
    path('sobre/', sobre ), #/sobre/
    path('contato/', contato ), #/contato/
]
