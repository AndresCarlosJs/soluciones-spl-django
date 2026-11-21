from unittest.mock import patch

from django.test import SimpleTestCase


class VariabilityTests(SimpleTestCase):
    def test_variant_a_hides_optional_components(self):
        with patch('core.views.ENABLE_REPORTS', False), patch('core.views.ENABLE_NOTIFICATIONS', False):
            response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Reportes y análisis')
        self.assertNotContains(response, 'Notificaciones')

    def test_variant_b_shows_optional_components(self):
        with patch('core.views.ENABLE_REPORTS', True), patch('core.views.ENABLE_NOTIFICATIONS', True):
            response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Reportes y análisis')
        self.assertContains(response, 'Notificaciones')
