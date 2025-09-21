# clients/urls.py (app file)
from django.urls import path
from .views import *

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='create-project'),
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
]