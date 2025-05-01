from django.test import TestCase


class LoginTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/login/')

    def test_get(self):
        """GET must return status code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use pages/login.html"""
        self.assertTemplateUsed(self.response, 'pages/login.html')