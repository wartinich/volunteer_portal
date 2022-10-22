import pytest

from datetime import date
from django.urls import reverse


@pytest.fixture
def auth_data():
    data = {
        "email": "test@gmail.com",
        "first_name": "Loli",
        "last_name": "Pup",
        "birth_date": date(2002, 12, 31),
        "password": "test_password",
        "is_active": True
    }
    return data


def test_sign_up(client, db, auth_data):
    resp = client.post(reverse("authentication:sign_up"), data=auth_data)
    assert resp.status_code == 200
