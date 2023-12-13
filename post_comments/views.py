from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from gamer_connect_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import PostCommentSerializer, PostCommentDetailSerializer


class PostCommentList(generics.ListCreateAPIView):
    """
    List all comments or create a comment if the user is logged in.
    """
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend
        ]
    filterset_fields = [
        'post'
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a comment by id if the user owns the comment
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostCommentDetailSerializer
    queryset = Comment.objects.all()
