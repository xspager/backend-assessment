import base64

from django.test import TestCase


class TestActivation(TestCase):

    fixtures = ['main/test_fixtures.json',]

    def tearDown(self):
        self.client.session.clear()

    def test_nonexisting_basic_login(self):
        user_pass = "foo:bar"
        
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        response = self.client.post('/product/activate', **auth_headers)

        self.assertEqual(401, response.status_code)

    def test_existing_basic_login(self):
        user_pass = "bob:tables123"
        
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        response = self.client.post('/product/activate', **auth_headers)
    
        self.assertEqual(201, response.status_code)
        self.assertEqual({}, response.json())

    def test_invalid_jwt_authentication(self):
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Berer nemo',
        }

        response = self.client.post('/product/activate', **auth_headers)
        
        self.assertNotEqual(201, response.status_code)

    def test_valid_jwt_autherication(self):
        response = self.client.post('/api/token/', {'username': 'bob', 'password': 'tables123'})

        self.assertEqual(200, response.status_code)
        token_resp = response.json()

        self.assertNotEqual({}, token_resp)

        auth_header = {
            'HTTP_AUTHORIZATION': 'Bearer ' + token_resp['access'],
        }

        response = self.client.post('/product/activate', **auth_header)

        self.assertEqual(201, response.status_code)
    
    def test_do_not_accept_get(self):
        user_pass = "bob:tables123"
        
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + base64.b64encode(user_pass.encode()).decode('ascii')
        }

        response = self.client.get('/product/activate', **auth_headers)
        
        # 405 Method Not Allowed
        self.assertEqual(405, response.status_code)

