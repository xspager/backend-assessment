import base64
import json

from unittest import skip

from django.test import TestCase


class TestActivation(TestCase):
    fixtures = [
        'main/test/users_fixtures.json',
        'main/test/activation_fixtures.json',
    ]
    
    def test_do_not_accept_get(self):
        user_pass = "bob:tables123"
        
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        response = self.client.get('/product/activate', **auth_headers)
        
        # 405 Method Not Allowed
        self.assertEqual(405, response.status_code)


    def test_activation_with_valid_user(self):
        user_pass = "bob:tables123"
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        activation_request = {
            "partner": 1,
            "customer": 1
        }

        response = self.client.post('/product/activate', data=json.dumps(activation_request), content_type="application/json", **auth_headers)
        
        self.assertEqual(201, response.status_code)
        self.assertIn("id", response.json())
