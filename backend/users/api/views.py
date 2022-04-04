from rest_framework import generics, filters
from base.permissions import IsAuthor
from users.api.serializers import UserProfileSerializer, UpdateUserProfileSerializer, UserListSerializer
from users.models import User


class UserListView(generics.ListAPIView):
    """List of all users"""
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'first_name', 'last_name']
    ordering_fields = ['verified']


class UserDetailView(generics.RetrieveAPIView):
    """User detail info"""
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()


class UserUpdateView(generics.UpdateAPIView):
    """Update user info"""
    serializer_class = UpdateUserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthor]
