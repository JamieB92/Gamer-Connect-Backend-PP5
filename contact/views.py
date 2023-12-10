from rest_framework import generics, permissions
from gamer_connect_api.permissions import IsOwnerOrReadOnly
from .models import Contact
from .serializers import ContactFormSerializer


class ListContacts(generics.ListCreateAPIView):
    """
    Displays all contacts that have been sent through
    Allows the user create a contact if logged in
    """
    serializer_class = ContactFormSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an update.
    From here delete and update is availbe
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ContactFormSerializer
    queryset = Contact.objects.all()