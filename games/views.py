from rest_framework import generics, permissions
from gamer_connect_api.permissions import IsOwnerOrReadOnly
from .models import Games
from .serializers import GamesSerializer

# Create your views here.
class GamesList(generics.ListCreateAPIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Games.objects.all()
    serializer_class = GamesSerializer