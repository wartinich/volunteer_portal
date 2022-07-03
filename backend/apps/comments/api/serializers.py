from rest_framework import serializers

from apps.base.serializers import UserInfoSerializer, RecursiveSerializer
from apps.comments.models import Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    """Serialize data for create comment"""
    class Meta:
        model = Comment
        fields = ('aid', 'message', 'parent')


class CommentSerializer(serializers.ModelSerializer):
    """Serialize data of comment"""
    user = UserInfoSerializer()
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('id', 'aid', 'user', 'message', 'children')
