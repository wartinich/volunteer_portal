import pytest

from django.contrib.auth.hashers import make_password

from mixer.backend.django import mixer


@pytest.fixture
def create_and_login(client, db):
    email = "test@gmail.com"
    password = "password"
    hash_password = make_password(password=password)
    user = mixer.blend('authentication.User', email=email, password=hash_password, is_active=True)
    client.login(email=email, password=password)
    return user
