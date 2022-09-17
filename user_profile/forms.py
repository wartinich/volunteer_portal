from django import forms

from authentication.models import User


class UserForm(forms.ModelForm):
    user_photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["user_photo", "email", "first_name", "last_name", "birth_date", "bio"]
