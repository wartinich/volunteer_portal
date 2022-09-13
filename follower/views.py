from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from authentication.models import User
from follower.models import Follower


class AddFollower(LoginRequiredMixin, View):
    """Add follower"""

    def post(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)
        Follower.objects.create(subscriber=request.user, user=user)
        return redirect("user:user-detail", pk=user.pk)


class RemoveFollower(LoginRequiredMixin, View):
    """Remove follower"""

    def post(self, request, pk, *args, **kwargs):
        Follower.objects.filter(subscriber=request.user, user_id=pk).delete()
        return redirect("user:user-detail", pk=pk)
