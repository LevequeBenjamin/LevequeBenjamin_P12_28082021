"""Contains the urls of contracts app."""

# django
from django.urls import path

# views
from contracts.views import ContractListCreateView, ContractRetrieveUpdateDestroyView

urlpatterns = [
    # GET, POST
    path('contracts/', ContractListCreateView.as_view(), name="list_create_contract"),
    # GET, PUT, PATCH, DELETE
    path('contracts/<int:pk>/', ContractRetrieveUpdateDestroyView.as_view(),
         name="update_destroy_retrieve_contract"),
]
