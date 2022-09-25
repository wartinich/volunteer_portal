from django.urls import path
from user_profile.views.verify import VerifyUser, verify_user

verify_patterns = [
    path("verify/", VerifyUser.as_view(), name="verify-user"),
    path("verify-user/<uidb64>/<token>/", verify_user, name='verify'),
]
