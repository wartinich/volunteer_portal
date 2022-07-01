from rest_framework import serializers
from assistances.models import Aid, Category
from comments.api.serializers import CommentSerializer
from base.serializers import UserInfoSerializer


class CategorySerializer(serializers.ModelSerializer):
    """Serializer category data"""
    class Meta:
        model = Category
        fields = ('name',)


class CreateAidSerializer(serializers.ModelSerializer):
    """Serialize data for create aid"""
    class Meta:
        model = Aid
        fields = ('title', 'description', 'cover', 'payment_url', 'category')


class AidSerializer(serializers.ModelSerializer):
    """Serialize data for aids list"""
    category = CategorySerializer()
    user = UserInfoSerializer()

    class Meta:
        model = Aid
        fields = ('id', 'title', 'cover', 'user', 'category', 'comments_count', 'created_at')


class DetailAidSerializer(serializers.ModelSerializer):
    """Serialize data for all aid info"""
    user = UserInfoSerializer()
    category = CategorySerializer()
    comment_aid = CommentSerializer(many=True)

    class Meta:
        model = Aid
        fields = ('id', 'title', 'cover', 'description', 'user', 'category', 'payment_url', 'comments_count', 'comment_aid', 'created_at')
