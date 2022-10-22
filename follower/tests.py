import pytest

from django.urls import reverse
from mixer.backend.django import mixer
from django.contrib.auth.hashers import make_password

from follower.models import Follower


@pytest.fixture
def new_follower(db):
    email = "test@gmail.com"
    password = "password"
    hash_password = make_password(password=password)
    return mixer.blend('authentication.User', email=email, password=hash_password, is_active=True)


@pytest.fixture
def follower_data():
    user = mixer.blend("authentication.User")
    return {"user": user.id}


def test_add_follower(client, db, create_and_login, follower_data):
    resp = client.post(reverse("follower:follower-add", args=(follower_data["user"],)), data=follower_data)
    assert resp.status_code == 302
    follower = Follower.objects.get(subscriber_id=create_and_login)
    assert follower.user.id == follower_data["user"]


def test_add_follower_no_access(client, db, follower_data):
    add_follower_url = reverse("follower:follower-add", args=(follower_data["user"],))
    resp = client.post(add_follower_url, data=follower_data)
    assert resp.status_code == 302
    assert resp.url == reverse("authentication:login") + "?next=" + add_follower_url


def test_remove_follower(client, db, create_and_login, follower_data):
    resp = client.post(reverse("follower:follower-add", args=(follower_data["user"],)), data=follower_data)
    assert resp.status_code == 302
    follower = Follower.objects.get(subscriber_id=create_and_login)
    assert follower.user.id == follower_data["user"]


def test_remove_follower_no_access(client, db, follower_data):
    remove_follower_url = reverse("follower:follower-add", args=(follower_data["user"],))
    resp = client.post(remove_follower_url, data=follower_data)
    assert resp.status_code == 302
    assert resp.url == reverse("authentication:login") + "?next=" + remove_follower_url
