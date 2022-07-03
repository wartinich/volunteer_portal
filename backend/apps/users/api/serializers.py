from rest_framework import serializers
from apps.assistances.api.serializers import DetailAidSerializer
from apps.users.models import User


class UserListSerializer(serializers.ModelSerializer):
    """Serializer data for list of users"""
    class Meta:
        model = User
        fields = ('id', 'user_photo', 'username', 'first_name', 'last_name', 'verified')


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize detail data for user"""
    aids = DetailAidSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'user_photo', 'first_name', 'last_name', 'username', 'date_of_birth', 'phone_number', 'telegram_username', 'verified', 'aids')


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    """Serialize data for update user"""
    class Meta:
        model = User
        fields = ('username', 'user_photo', 'phone_number', 'telegram_username')