from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from accounts.permissions import IsSales
from clients.models import Client
from contracts.serializers import ContractSerializer


class ContractListCreateView(ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a Contract instance.
    """

    # Overrides attribute in GenericAPIView.
    serializer_class = ContractSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsSales]

    # Overrides method in CreateModelMixin.
    def perform_create(self, serializer):
        """
        Override of the perform_create method to add the author.
        """
        client = get_object_or_404(Client, pk=self.request.data.get("client"))
        serializer.save(client=client, sales_contact=self.request.user)


class ContractRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a Contract instance.
    """

    # Overrides attributes in GenerateAPIView
    serializer_class = ContractSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsSales]