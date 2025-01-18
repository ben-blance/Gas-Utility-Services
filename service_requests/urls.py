# service_requests/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_request, name='track_request'),
    path('confirmation/<uuid:tracking_id>/', views.request_confirmation, name='request_confirmation'),
]
