from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from assistance.forms import AssistanceForm
from assistance.models import Assistance


class AssistanceCreateView(LoginRequiredMixin, CreateView):
    """Create assistance"""

    model = Assistance
    template_name = "assistance/assistance_create_form.html"
    form_class = AssistanceForm
    success_url = reverse_lazy("assistance:assistance-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AssistanceListView(LoginRequiredMixin, ListView):
    """Get list of assistance"""

    model = Assistance
    template_name = "assistance/assistance_list.html"
    paginate_by = 6

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


class AssistanceUpdateView(LoginRequiredMixin, UpdateView):
    """Update assistance data"""

    model = Assistance
    form_class = AssistanceForm
    template_name = "assistance/assistance_update_form.html"
    context_object_name = "assistance"

    def get_success_url(self):
        return reverse_lazy("assistance:assistance-detail", kwargs={"pk": self.kwargs["pk"]})

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs["pk"])


class AssistanceDeleteView(LoginRequiredMixin, DeleteView):
    """Delete assistance"""

    model = Assistance
    success_url = reverse_lazy("assistance:assistance-list")

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs["pk"])
