from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from authentication.models import User


class ProfileView(LoginRequiredMixin, TemplateView):
    """Get user data"""

    template_name = "user_profile/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["user"] = self.request.user

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Update user data"""

    model = User
    fields = ["email", "first_name", "last_name", "birth_date", "user_photo"]
    template_name = "user_profile/profile_update_form.html"
    success_url = reverse_lazy("user_profile:profile-update")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form = super().form_valid(form)
        message = "Personal Information has been updated"
        messages.success(request=self.request, message=message)
        return form


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """Update user password"""

    template_name = "user_profile/password_change_form.html"
    success_url = reverse_lazy("user_profile:password-change")

    def form_valid(self, form):
        form = super().form_valid(form)
        message = "The password has been successfully updated"
        messages.success(request=self.request, message=message)
        return form
