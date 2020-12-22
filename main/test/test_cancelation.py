import base64
import json

from unittest import skip

from django.test import TestCase


class TestCancelation(TestCase):
    fixtures = [
        'main/test/users_fixtures.json',
        'main/test/activation_fixtures.json',
    ]

    def test_logical_delete_on_cancelation(self):
        # FIXME: Is canceletion a status change or a delete?
        user_pass = "bob:tables123"
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        from ..models import Activation

        activation = Activation.objects.create(partner_id=1, customer_id=1)

        response = self.client.delete(f'/product/activate/{activation.pk}', content_type="application/json", **auth_headers)
        
        self.assertEqual(204, response.status_code)

        self.assertEqual(True, Activation.objects.get(pk=activation.pk).deleted)
