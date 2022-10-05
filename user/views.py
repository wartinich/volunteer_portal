from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from assistance.models import Assistance
from authentication.models import User
from follower.models import Follower
from user.filters import UserFilter


class UserListView(LoginRequiredMixin, ListView):
    """Get list of user"""

    model = User
    paginate_by = 3
    template_name = "user/user_list.html"

    def get_queryset(self):
        queryset = self.model.objects.all()
        f = UserFilter(self.request.GET, queryset)
        return f.qs


class UserDetailView(LoginRequiredMixin, DetailView):
    """Get user data"""

    model = User
    template_name = "user/user_detail.html"
    context_object_name = "user"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(self.model, pk=self.kwargs["pk"])
        context["assistance"] = Assistance.objects.filter(user_id=self.kwargs["pk"])
        context["assistance_count"] = Assistance.objects.filter(user_id=self.kwargs["pk"]).count()
        context["follower_count"] = Follower.objects.filter(user_id=self.kwargs["pk"]).count()
        context["following_count"] = Follower.objects.filter(subscriber_id=self.kwargs["pk"]).count()
        context["is_following"] = Follower.objects.filter(
            subscriber=self.request.user,
            user_id=self.kwargs["pk"]
        )
        return context
