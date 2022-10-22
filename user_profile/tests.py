import pytest

from django.urls import reverse
from mixer.backend.django import mixer


@pytest.fixture
def new_user(db):
    return mixer.blend("authentication.User", email="new_user@mail.com", is_verified=True)


def test_get_user_profile(client, db, create_and_login):
    resp = client.get(reverse("user_profile:profile"))
    assert resp.status_code == 200


def test_get_user_profile_no_access(client, db):
    profile_url = reverse("user_profile:profile")
    resp = client.get(profile_url)
    assert resp.status_code == 302
    assert resp.url == reverse("authentication:login") + "?next=" + profile_url
