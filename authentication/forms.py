from django.contrib.auth.forms import UserCreationForm

from authentication.models import User


class UserRegisterForm(UserCreationForm):
    """Custom UserCreationForm"""

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "birth_date",
            "password1",
            "password2"
        ]
