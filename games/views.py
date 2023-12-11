from rest_framework import generics, permissions
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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Games Detail View
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Games.objects.all()
    serializer_class = GamesSerializer