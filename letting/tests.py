
from django.test import TestCase
from django.urls import reverse

from . models import Letting


class TestLettings(TestCase):
    """Test Lettings URL"""

    def test_index(self):
        """
        page should contain <title>Lettings</title>
        """
        response = self.client.get(reverse('letting:lettings_index'))
        assert response.status_code == 200
        self.assertEqual(True, b'<title>Lettings</title>' in response.content)

    def test_lettings(self):
        """
        page should contain <title>lettings title value</title>
        """
        Lettings_tests = Letting.objects.all()
        for letting in Lettings_tests:
            response = self.client.get(reverse('lettings:letting', args=[letting.id]))
            assert response.status_code == 200
            self.assertInHTML(letting.title, str(response.content))
