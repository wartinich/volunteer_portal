from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from authentication.models import User
from follower.models import Follower


class AddFollower(LoginRequiredMixin, View):
    """Add follower"""
    def post(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)
        Follower.objects.create(subscriber=request.user, user=user)


class RemoveFollower(LoginRequiredMixin, View):
    """Remove follower"""
    def post(self, request, pk, *args, **kwargs):
        subscriber = Follower.objects.get(subscriber=request.user, user_id=pk)
        subscriber.delete()
