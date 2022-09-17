from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from assistance.models import Assistance
from authentication.models import User
from follower.models import Follower
from user_profile.forms import UserForm


class ProfileView(LoginRequiredMixin, TemplateView):
    """Get user data"""

    template_name = "user_profile/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["assistance"] = Assistance.objects.filter(user=self.request.user)
        context["assistance_count"] = Assistance.objects.filter(user=self.request.user).count()
        context["follower_count"] = Follower.objects.filter(user=self.request.user).count()
        context["following_count"] = Follower.objects.filter(subscriber=self.request.user).count()
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Update user data"""

    model = User
    form_class = UserForm
    template_name = "user_profile/profile_update_form.html"
    success_url = reverse_lazy("user_profile:profile")

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
