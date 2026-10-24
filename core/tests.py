from django.test import TestCase


class PublicApiTests(TestCase):
    """
    Smoke tests for the read-only endpoints consumed by the Vue client
    """

    def test_router_endpoints_are_public(self):
        endpoints = [
            'groups', 'works', 'skills', 'projects',
            'pages/navbar', 'pages/footer', 'pages/cookie-element', 'pages/rate',
            'pages/main', 'pages/projects', 'pages/skills', 'pages/about',
            'pages/terms', 'pages/privacy', 'pages/cookies',
        ]
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(f'/api/v1/{endpoint}/?language=en')
                self.assertEqual(response.status_code, 200)

    def test_router_endpoints_are_read_only_for_anonymous(self):
        response = self.client.post('/api/v1/projects/', {'name': 'x'})
        self.assertIn(response.status_code, (401, 403))

    def test_ascii_parts_have_expected_shape(self):
        for key in range(1, 21):
            with self.subTest(key=key):
                data = self.client.get(f'/api/v1/get_ascii_part_{key}').json()
                self.assertEqual(data['key'], key)
                self.assertTrue(data['res'])
                for frame in data['res']:
                    self.assertEqual(len(frame), 69)

    def test_ascii_unknown_part(self):
        data = self.client.get('/api/v1/get_ascii_part_999').json()
        self.assertIn('error', data)
