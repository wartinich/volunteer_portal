import pytest

from django.urls import reverse
from mixer.backend.django import mixer


@pytest.fixture
def new_user(db):
    return mixer.blend("authentication.User")


def test_get_user_list(client, db, create_and_login):
    resp = client.get(reverse("user:user-list"))
    assert resp.status_code == 200


def test_get_user_list_no_access(client, db):
    list_url = reverse("user:user-list")
    resp = client.get(list_url)
    assert resp.status_code == 302
    assert resp.url == reverse("authentication:login") + "?next=" + list_url


def test_get_user(client, create_and_login, new_user):
    resp = client.get(reverse("user:user-detail", args=(new_user.id,)))
    assert resp.status_code == 200


def test_get_user_wrong(client, create_and_login):
    resp = client.get(reverse("user:user-detail", args=(999,)))
    assert resp.status_code == 404


def test_get_user_no_access(client, new_user):
    detail_url = reverse("user:user-detail", args=(new_user.id,))
    resp = client.get(detail_url)
    assert resp.status_code == 302
    assert resp.url == reverse("authentication:login") + "?next=" + detail_url
