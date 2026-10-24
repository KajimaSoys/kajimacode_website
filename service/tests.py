from unittest import mock

from django.test import TestCase

from service.models import Feedback, Order, Rate


class ServiceApiTests(TestCase):
    """
    The client posts every form as {"request": {...}}
    """

    meta = {
        'project_version': '5.6',
        'user_agent': 'test',
        'screen_resolution': '1920x1080',
        'browser_language': 'en',
        'timezone': 'Europe/Moscow',
    }

    @mock.patch('service.views.telepush_send')
    def test_send_request(self, telepush_send):
        body = {'request': {'name': 'Name', 'mail': 'mail@example.com', 'message': 'Hi', 'cookie': '', **self.meta}}
        response = self.client.post('/api/v1/send_request', body, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.count(), 1)
        telepush_send.assert_called_once()

    @mock.patch('service.views.telepush_send')
    def test_send_request_invalid(self, telepush_send):
        response = self.client.post('/api/v1/send_request', {'request': {}}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Order.objects.count(), 0)
        telepush_send.assert_not_called()

    def test_send_rate(self):
        body = {'request': {'source': 'about', 'rate_value': 5, **self.meta}}
        response = self.client.post('/api/v1/send_rate', body, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Rate.objects.get().rate_value, 5)

    def test_send_feedback(self):
        body = {'request': {'source': 'about', 'rate_message': 'Nice', **self.meta}}
        response = self.client.post('/api/v1/send_feedback', body, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Feedback.objects.get().rate_message, 'Nice')
