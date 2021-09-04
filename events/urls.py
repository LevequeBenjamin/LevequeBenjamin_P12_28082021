"""Contains the urls of events app."""

# django
from django.urls import path

# views
from events.views import EventListCreateView, EventRetrieveUpdateDestroyView

urlpatterns = [
    # GET, POST
    path('events/', EventListCreateView.as_view(), name="list_create_event"),
    # GET, PUT, PATCH, DELETE
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(),
         name="update_destroy_retrieve_event"),
]
