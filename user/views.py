from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from authentication.models import User


class UserListView(LoginRequiredMixin, ListView):
    """Get list of user"""

    model = User
    template_name = "user/user_list.html"

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class UserDetailView(LoginRequiredMixin, DetailView):
    """Get user data"""

    model = User
    template_name = "user/user_detail.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(self.model, pk=self.kwargs["pk"])
        return context
