from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminDashboardTests(TestCase):

    # setup function runs before every test
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@lrbc.ml",
            password="Password@123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@lrbc.ml",
            password="password123",
            name="Test User"
        )

    def test_users_listed(self):
        """Test that users are listed on the admin page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_user_edit_page(self):
        """Test that use edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
