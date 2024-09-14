# from django.urls import path
# from .views import api

# urlpatterns = [
#     path('random-word/', api, name='random-word'),
    
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('llm-api/', views.api, name='llm-api'),  # Route for the LLM API
]


