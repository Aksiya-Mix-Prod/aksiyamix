from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch

from apps.notifications.models import Notification


class NotificationTestCase(APITestCase):
    def setUp(self):
        """Test setup."""
        # Bu yerda test uchun zarur bo'lgan ma'lumotlarni yaratishingiz mumkin
        self.notification_data = {
            'title': 'Test Notification',
            'message': 'This is a test notification message.',
            'notification_type': 'LOGIN',  # Masalan, LOGIN turidagi xabar
            'user': 1,  # Bu foydalanuvchining ID sini o'zgartiring
        }

    @patch('fcm_django.models.FCMDevice.send_message')
    def test_create_notification(self, mock_send_message):
        """Test notification creation and sending."""

        # Create notification
        url = reverse('notification-list')  # Bu yerda URL nomi to'g'ri bo'lishi kerak
        response = self.client.post(url, self.notification_data, format='json')

        # Check if notification creation was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notification.objects.count(), 1)

        # Check that the send_message method was called
        mock_send_message.assert_called_once()
