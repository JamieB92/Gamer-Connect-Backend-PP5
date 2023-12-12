from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from gamer_connect_api.permissions import IsOwnerOrReadOnly
from .models import Games
from .serializers import GamesSerializer


class GamesList(generics.ListCreateAPIView):
    """
    Games list View
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    filter_backends = [
        DjangoFilterBackend
        ]
    filterset_fields = [
        'owner__username',
        'name',
        'friends',
        'experience'
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Games Detail View
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Games.objects.all()
    serializer_class = GamesSerializer