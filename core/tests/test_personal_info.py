from django.test import TestCase, Client
from django.urls import reverse
from ..models import PersonalInfo
import json


class TestPersonalInfo(TestCase):
    def setUp(self):
        self.client = Client()
        self.personal_info1 = PersonalInfo.objects.create(name="John Doe", address="123 Main St",
                                                          email="john@example.com", phone="1234567890")
        self.personal_info2 = PersonalInfo.objects.create(name="Jane Doe", address="456 Main St",
                                                          email="jane@example.com", phone="0987654321")

    def test_get_all_personal_info(self):
        response = self.client.get(reverse('personalinfo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_get_single_personal_info(self):
        response = self.client.get(reverse('personalinfo-detail', args=[self.personal_info1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_post_personal_info(self):
        personal_info_data = {
            "name": "Test User",
            "address": "789 Main St",
            "email": "test@example.com",
            "phone": "1122334455"
        }
        response = self.client.post(reverse('personalinfo-list'), data=json.dumps(personal_info_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Test User')
