from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from assistance.models import Assistance


class AssistanceCreateView(LoginRequiredMixin, CreateView):
    """Create assistance"""

    model = Assistance
    template_name = "assistance/assistance_create_form.html"


class AssistanceListView(LoginRequiredMixin, ListView):
    """Get list of assistance"""

    model = Assistance
    template_name = "assistance/assistance_list.html"

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class AssistanceDetailView(LoginRequiredMixin, DetailView):
    """Get assistance data"""

    model = Assistance
    template_name = "assistance/assistance_detail.html"
    context_object_name = "assistance"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs["pk"])


class AssistanceDeleteView(LoginRequiredMixin, DeleteView):
    """Delete assistance"""

    model = Assistance
    success_url = reverse_lazy("assistance:assistance-list")

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs["pk"])

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        message = "Assistance has been deleted"
        messages.success(request=self.request, message=message)
        return response
