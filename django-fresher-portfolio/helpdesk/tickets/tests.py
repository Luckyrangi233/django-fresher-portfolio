from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Ticket


class TicketWorkflowTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.owner = User.objects.create_user(username="owner", password="safe-test-password")
        self.other = User.objects.create_user(username="other", password="safe-test-password")
        self.ticket = Ticket.objects.create(title="Printer is offline", description="Room 2", created_by=self.owner)

    def test_login_required_for_list(self):
        response = self.client.get(reverse("ticket-list"))
        self.assertEqual(response.status_code, 302)

    def test_user_only_sees_own_tickets(self):
        self.client.force_login(self.other)
        response = self.client.get(reverse("ticket-list"))
        self.assertNotContains(response, self.ticket.title)

    def test_cannot_view_another_users_ticket(self):
        self.client.force_login(self.other)
        response = self.client.get(reverse("ticket-detail", args=[self.ticket.pk]))
        self.assertEqual(response.status_code, 404)

    def test_create_assigns_current_user(self):
        self.client.force_login(self.owner)
        response = self.client.post(reverse("ticket-create"), {
            "title": "Cannot access account", "description": "Reset link fails", "priority": "high",
        })
        created = Ticket.objects.get(title="Cannot access account")
        self.assertEqual(created.created_by, self.owner)
        self.assertEqual(response.status_code, 302)

    def test_status_update_requires_post_and_valid_choice(self):
        self.client.force_login(self.owner)
        response = self.client.post(reverse("ticket-update-status", args=[self.ticket.pk]), {"status": "resolved"})
        self.ticket.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.ticket.status, Ticket.Status.RESOLVED)
        self.client.post(reverse("ticket-update-status", args=[self.ticket.pk]), {"status": "made_up"})
        self.ticket.refresh_from_db()
        self.assertEqual(self.ticket.status, Ticket.Status.RESOLVED)
