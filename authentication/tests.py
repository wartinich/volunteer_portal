import pytest

from django.urls import reverse


@pytest.fixture
def auth_data():
    return {
        "username": "test@gmail.com",
        "password": "password"
    }


def test_login(client, auth_data):
    resp = client.post(reverse("authentication:login"), data=auth_data)
    assert resp.status_code == 200


def test_username_not_valid(client, db, auth_data):
    auth_data["username"] = "wrong_email@gmail.com"
    resp = client.post(reverse("authentication:login"), data=auth_data)
    assert resp.status_code == 200


def test_password_not_valid(client, db, auth_data):
    auth_data["password"] = "wrong_password"
    resp = client.post(reverse("authentication:login"), data=auth_data)
    assert resp.status_code == 200


def test_login_view(client):
    resp = client.get(reverse("authentication:login"))
    assert resp.status_code == 200


def test_login_view_no_access(client):
    resp = client.get(reverse("authentication:login"))
    assert resp.status_code == 404
