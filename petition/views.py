from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from petition.models import Petition


class PetitionListView(LoginRequiredMixin, ListView):
    """Get list of petition"""

    model = Petition
    template_name = "petition/petition_list.html"

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class PetitionDetailView(LoginRequiredMixin, DetailView):
    """Get petition data"""

    model = Petition
    template_name = "petition/petition_detail.html"
    context_object_name = "assistance"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs["pk"])
