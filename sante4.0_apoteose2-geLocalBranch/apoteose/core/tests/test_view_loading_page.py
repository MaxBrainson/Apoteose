from django.test import TestCase

class LoadingTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use initial_loading.html"""
        self.assertTemplateUsed(self.response, 'initial_loading.html')



