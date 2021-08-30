from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from accounts.permissions import IsSales, IsSupport
from clients.models import Client
from contracts.models import Contract
from events.serializers import EventSerializer


class EventListCreateView(ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a Contract instance.
    """

    # Overrides attribute in GenericAPIView.
    serializer_class = EventSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsSales]

    # Overrides method in CreateModelMixin.
    def perform_create(self, serializer):
        """
        Override of the perform_create method to add the author.
        """
        client = get_object_or_404(Client, pk=self.request.data.get("client"))
        contract = get_object_or_404(Contract, pk=self.request.data.get("contract"))
        support_contact = get_object_or_404(User, pk=self.request.data.get("support_contact"))
        serializer.save(client=client, contract=contract, support_contact=support_contact)


class EventRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a Event instance.
    """

    # Overrides attributes in GenerateAPIView
    serializer_class = EventSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsSales, IsSupport]

    # Overrides method in UpdateModelMixin.
    def perform_update(self, serializer):
        """
        Override of the perform_create method to add the author.
        """
        support_contact = get_object_or_404(User, pk=self.request.data.get("support_contact"))
        serializer.save(support_contact=support_contact)
