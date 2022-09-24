from rest_framework import viewsets

from api.serializers import AssistanceSerializer
from assistance.models import Assistance


class AssistanceViewSet(viewsets.ModelViewSet):
    serializer_class = AssistanceSerializer
    queryset = Assistance.objects.all()
