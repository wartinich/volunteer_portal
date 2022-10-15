import pytest

from django.urls import reverse
from mixer.backend.django import mixer


@pytest.fixture
def new_assistance(db):
    return mixer.blend("assistance.Assistance")


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
