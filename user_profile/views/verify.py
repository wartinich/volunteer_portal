from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View

from authentication.models import User
from user_profile.services.utils import generate_token
from user_profile.tasks import send_verify_email


class VerifyUser(View):
    def post(self, request, *args, **kwargs):
        send_verify_email(user=request.user, request=request)
        return reverse_lazy("user_profile:profile")


def verify_user(uidb64, token):
    uid = str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    if user and generate_token.check_token(user, token):
        user.is_verified = True
        user.save()

        return reverse_lazy('user_profile:profile')
