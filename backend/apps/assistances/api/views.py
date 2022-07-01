from rest_framework import generics, permissions, filters
from apps.base.permissions import IsAuthor
from apps.assistances.api.serializers import CreateAidSerializer, AidSerializer, DetailAidSerializer
from apps.assistances.models import Aid


class CreateAidView(generics.CreateAPIView):
    """Create aid"""
    serializer_class = CreateAidSerializer
    queryset = Aid.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListAidView(generics.ListAPIView):
    """List of all aids"""
    serializer_class = AidSerializer
    queryset = Aid.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'user', 'category']
    ordering_fields = ['id', 'category', 'created_at']


class DetailAidView(generics.RetrieveAPIView):
    """Detail info about aid"""
    serializer_class = DetailAidSerializer
    queryset = Aid.objects.all()
    lookup_field = 'id'


class UpdateAidView(generics.UpdateAPIView):
    """Update aid info"""
    serializer_class = CreateAidSerializer
    queryset = Aid.objects.all()
    permission_classes = [IsAuthor]
    lookup_field = 'id'
