from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Camping
from rest_framework.test import APIClient
from rest_framework import status

CAMPING_URL = "/api/camping"


def create_user(email="user1@example.com", password="test123!@#"):
    default = dict(email=email, password=password)
    user = get_user_model().objects.create_user(**default)
    return user


def create_camping(user, **kwargs):
    defaults = dict(
        title="DeepForest",
        visited_dt="2022-12-03",
        review="Some Review",
        price=5000,
    )
    defaults.update(kwargs)
    camping = Camping.objects.create(user=user, **defaults)
    return camping


class PrivateCampingAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user()
        self.client.force_authenticate(self.user)

    def test_create_camping(self):
        payload = dict(
            title="DeepForest",
            visited_dt="2022-12-03",
            review="some review",
            price=5000,
        )
        res = self.client.post(CAMPING_URL, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        camping = Camping.objects.get(id=res.data.get("id"))
        for k, v in payload.items():
            self.assertEqual(getattr(camping, k), v)
        self.assertEqual(camping.user, self.user)
