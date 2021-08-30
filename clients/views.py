"""Contains the views of client app."""

# rest_framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

# serializers
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from accounts.permissions import IsSales
from clients.models import Client
from clients.serializers import ClientSerializer


class ClientListCreateView(ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a Client instance.
    """

    # Overrides attributes in GenerateAPIView
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsSales]

    # Overrides method in CreateModelMixin.
    def perform_create(self, serializer):
        """
        Override of the perform_create method to add the author.
        """
        sales_contact = get_object_or_404(User, pk=self.request.data.get("sales_contact"))
        serializer.save(sales_contact=sales_contact)


class ClientRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a Client instance.
    """

    # Overrides attributes in GenerateAPIView
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsSales]

    # Overrides method in UpdateModelMixin.
    def perform_update(self, serializer):
        """
        Override of the perform_create method to add the author.
        """
        sales_contact = get_object_or_404(User, pk=self.request.data.get("sales_contact"))
        serializer.save(sales_contact=sales_contact)
