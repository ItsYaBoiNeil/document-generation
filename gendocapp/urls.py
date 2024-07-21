from django.urls import path
from .views import api

urlpatterns = [
    path('random-word/', api, name='random-word'),
]