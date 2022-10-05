import django_filters

from assistance.models import Assistance


class AssistanceFilter(django_filters.FilterSet):
    class Meta:
        model = Assistance
        fields = {
            "name": ["icontains"],
        }
