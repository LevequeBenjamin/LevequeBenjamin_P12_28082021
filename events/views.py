"""Contains the views of events app."""

# rest_framework
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _

# models
from accounts.models import User
from clients.models import Client
from contracts.models import Contract

# permissions
from accounts.permissions import IsSupport, IsClientContact

# serializers
from events.models import Event
from events.serializers import EventSerializer


class EventListCreateView(ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a Event instance.
    """

    # Overrides attributes in GenericAPIView.
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsClientContact]

    def perform_create(self, serializer):
        """Overrides method in CreateModelMixin."""
        client = get_object_or_404(Client, pk=self.request.data.get("client"))
        contract = get_object_or_404(Contract, pk=self.request.data.get("contract"))
        if client != contract.client:
            raise ValidationError(_("This client is not part of this contract!"))
        support_contact = get_object_or_404(User, pk=self.request.data.get("support_contact"))
        if support_contact.role != 3:
            raise ValidationError(_("This user is not part of the support team!"))
        serializer.save(client=contract.client, contract=contract, support_contact=support_contact)


class EventRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a Event instance.
    """

    # Overrides attributes in GenerateAPIView
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsSupport]
