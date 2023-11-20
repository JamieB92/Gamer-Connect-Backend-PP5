from rest_framework import generics, permissions
from gamer_connect_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import PostCommentSerializer

class PostCommentList(generics.ListCreateAPIView):
    """
    List posts_comments or create a comment if logged in.
    """
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
