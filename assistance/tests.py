import pytest

from django.urls import reverse
from mixer.backend.django import mixer

from assistance.constants import AssistanceStatus
from assistance.models import Assistance


@pytest.fixture
def new_assistance(db):
    return mixer.blend("assistance.Assistance")


@pytest.fixture
def assistance_data():
    category = mixer.blend("assistance.Category")
    return {
        "name": "Test name",
        "description": "Test desciption",
        "category": category.id,
        "payment_url": "https://www.monobank.ua/",
        "status": AssistanceStatus.ASSISTANCE_IPS.name
    }


def test_create_assistance(client, db, create_and_login, assistance_data):
    resp = client.post(reverse("assistance:assistance-create"), data=assistance_data)
    assert resp.status_code == 302
    assistance = Assistance.objects.get(user_id=create_and_login)
    assert assistance.name == assistance_data["name"]
    assert assistance.description == assistance_data["description"]
    assert assistance.category.id == assistance_data["category"]
    assert assistance.payment_url == assistance_data["payment_url"]
    assert assistance.status == assistance_data["status"]


def test_get_assistance(client, db, create_and_login, new_assistance):
    resp = client.get(reverse("assistance:assistance-detail", args=(new_assistance.id,)))
    assert resp.status_code == 200


def test_get_assistance_no_access(client, db, new_assistance):
    detail_url = reverse("assistance:assistance-detail", args=(new_assistance.id,))
    resp = client.get(detail_url)
    assert resp.status_code == 302
    assert resp.url == reverse("authentication:login") + "?next=" + detail_url


def test_get_wrong_assistance(client, db, create_and_login, new_assistance):
    resp = client.get(reverse("assistance:assistance-detail", args=(999,)))
    assert resp.status_code == 404


def test_get_assistance_list(client, create_and_login):
    resp = client.get(reverse("assistance:assistance-list"))
    assert resp.status_code == 200


def test_get_assistance_list_search(client, create_and_login, new_assistance):
    resp = client.get(f"{reverse('assistance:assistance-list')}?name__icontains=Test")
    assert resp.status_code == 200


def test_get_assistance_list_no_access(client):
    resp = client.get(reverse("assistance:assistance-list"))
    assert resp.status_code == 302


def test_update_assistance(client, db, create_and_login, new_assistance):
    category = mixer.blend("assistance.Category")

    updated_assistance_data = {
        "name": "Name test",
        "description": "Desciption test",
        "category": category.id,
        "payment_url": "https://www.monobank.ua/eu",
        "status": AssistanceStatus.ASSISTANCE_PAUSE.name,
    }
    resp = client.post(reverse("assistance:assistance-update", args=(new_assistance.id,)), data=updated_assistance_data)
    assert resp.status_code == 302

    new_assistance.refresh_from_db()
    assert new_assistance.name == updated_assistance_data["name"]
    assert new_assistance.description == updated_assistance_data["description"]
    assert new_assistance.category.id == updated_assistance_data["category"]
    assert new_assistance.payment_url == updated_assistance_data["payment_url"]
    assert new_assistance.status == updated_assistance_data["status"]


def test_update_assistance_no_access(client, new_assistance, assistance_data):
    delete_url = reverse("assistance:assistance-update", args=(new_assistance.id,))
    resp = client.post(delete_url, data=assistance_data)
    assert resp.status_code == 302
    assert resp.url == reverse("authentication:login") + "?next=" + delete_url


def test_delete_assistance(client, create_and_login, new_assistance):
    resp = client.delete(reverse("assistance:assistance-delete", args=(new_assistance.id,)))
    assert resp.status_code == 302


def test_delete_assistance_no_access(client, new_assistance):
    delete_url = reverse("assistance:assistance-delete", args=(new_assistance.id,))
    resp = client.delete(delete_url)
    assert resp.status_code == 302
    assert resp.url == reverse("authentication:login") + "?next=" + delete_url
