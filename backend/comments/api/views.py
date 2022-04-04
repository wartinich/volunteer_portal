from rest_framework import generics, permissions
from comments.api.serializers import CreateCommentSerializer
from comments.models import Comment


class CreateCommentView(generics.CreateAPIView):
    """Create comment"""
    serializer_class = CreateCommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
