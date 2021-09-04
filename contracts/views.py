"""Contains the views of contracts app."""

# rest_framework
from rest_framework.generics import ListCreateAPIView, get_object_or_404,\
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

# permissions
from accounts.permissions import IsClientContact

# models
from clients.models import Client
from contracts.models import Contract

# serializers
from contracts.serializers import ContractSerializer


class ContractListCreateView(ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a Contract instance.
    """

    # Overrides attribute in GenericAPIView.
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsClientContact]

    def perform_create(self, serializer):
        """Overrides method in CreateModelMixin."""
        client = get_object_or_404(Client, pk=self.request.data.get("client"))
        serializer.save(client=client, sales_contact=self.request.user)


class ContractRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a Contract instance.
    """

    # Overrides attributes in GenerateAPIView
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    # A user must be authenticated
    permission_classes = [IsAuthenticated, IsClientContact]
