"""Contains the urls of clients app."""

# django
from django.urls import path

# views
from clients.views import ClientListCreateView, ClientRetrieveUpdateDestroyView

urlpatterns = [
    # GET, POST
    path('clients/', ClientListCreateView.as_view(), name="list_create_client"),
    # GET, PUT, PATCH, DELETE
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(),
         name="update_destroy_retrieve_client"),
]
