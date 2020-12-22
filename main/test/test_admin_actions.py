import base64
import json

from unittest import skip

from django.test import TestCase


class TestAdminActions(TestCase):
    fixtures = [
        'main/test/users_fixtures.json',
        'main/test/activation_fixtures.json',
    ]

    def test_regular_user_cannot_change_status(self):
        user_pass = "bob:tables123"
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        from ..models import Activation

        activation = Activation.objects.create(partner_id=1, customer_id=1)

        response = self.client.post(f'/product/activation/approve/{activation.pk}', content_type="application/json", **auth_headers)
        
        self.assertEqual(403, response.status_code)

        self.assertEqual(Activation.StatusActivation.REQUESTED, Activation.objects.get(pk=activation.pk).status)

    def test_superuser_can_approve(self):
        user_pass = "superuser:tables123"
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        from ..models import Activation

        activation = Activation.objects.create(partner_id=1, customer_id=1)

        response = self.client.post(f'/product/activation/approve/{activation.pk}', content_type="application/json", **auth_headers)
        
        self.assertEqual(200, response.status_code)

        self.assertEqual(Activation.StatusActivation.APPROVED, Activation.objects.get(pk=activation.pk).status)


    def test_superuser_can_reject(self):
        user_pass = "superuser:tables123"
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        from ..models import Activation

        activation = Activation.objects.create(partner_id=1, customer_id=1)

        response = self.client.post(f'/product/activation/reject/{activation.pk}', content_type="application/json", **auth_headers)
        
        self.assertEqual(200, response.status_code)

        self.assertEqual(Activation.StatusActivation.REJECTED, Activation.objects.get(pk=activation.pk).status)

