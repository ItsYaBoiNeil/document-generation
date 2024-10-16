# from django.urls import path
# from .views import api

# urlpatterns = [
#     path('random-word/', api, name='random-word'),
    
# ]

from django.urls import path
from . import views

urlpatterns = [
    # path('llm-api/', views.api, name='llm-api'),
    path('', views.home, name='home'),
    path('process_question/', views.process_question, name='process_question'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),# Route for the LLM API
]






