from rest_framework import generics
from gamer_connect_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer



class AllProfiles(generics.ListAPIView):
    """
    Display all profiles
    Does not create view as profile creation done via django signals
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Displays an individual profile view
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer