from rest_framework import serializers
from users.models import User


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class UserInfoSerializer(serializers.ModelSerializer):
    """Serialize short data of user """
    class Meta:
        model = User
        fields = ('id', 'user_photo', 'username', 'first_name', 'last_name', 'verified')
