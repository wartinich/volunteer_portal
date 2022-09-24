from rest_framework import serializers

from assistance.models import Assistance
from authentication.models import User


class AuthorSerializer(serializers.ModelSerializer):
    """Serialize author data"""

    class Meta:
        model = User
        fields = ["full_name", "is_verified"]


class AssistanceSerializer(serializers.ModelSerializer):
    """Serialize assistance data"""

    user = AuthorSerializer()
    category = serializers.StringRelatedField()

    class Meta:
        model = Assistance
        fields = ["id", "image", "name", "description", "user", "category", "status", "updated_at"]
