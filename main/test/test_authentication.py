import base64
import json

from unittest import skip

from django.test import TestCase


class TestAuthentication(TestCase):

    fixtures = ['main/test/users_fixtures.json',]

    def tearDown(self):
        self.client.session.clear()

    def test_invalid_basic_login(self):
        user_pass = "foo:bar"
        
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        response = self.client.post('/product/activate', **auth_headers)

        self.assertEqual(401, response.status_code)

    def test_valid_basic_login(self):
        user_pass = "bob:tables123"
        
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        response = self.client.post('/product/activate', data=json.dumps({}), content_type="application/json", **auth_headers)
    
        self.assertNotEqual(401, response.status_code)

    def test_invalid_jwt_authentication(self):
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Berer nemo',
        }

        response = self.client.post('/product/activate', data=json.dumps({}), content_type="application/json", **auth_headers)
        
        self.assertNotEqual(201, response.status_code)

    def test_valid_jwt_autherication(self):
        response = self.client.post('/api/token/', {'username': 'bob', 'password': 'tables123'})

        self.assertEqual(200, response.status_code)
        token_resp = response.json()

        self.assertNotEqual({}, token_resp)

        auth_header = {
            'HTTP_AUTHORIZATION': 'Bearer ' + token_resp['access'],
        }

        response = self.client.post('/product/activate', data=json.dumps({}), content_type="application/json", **auth_header)

        self.assertNotEqual(401, response.status_code)
