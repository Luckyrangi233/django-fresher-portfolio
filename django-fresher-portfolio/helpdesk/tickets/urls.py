from django.urls import path
from . import views

urlpatterns = [
    path("", views.ticket_list, name="ticket-list"),
    path("tickets/new/", views.ticket_create, name="ticket-create"),
    path("tickets/<int:pk>/", views.ticket_detail, name="ticket-detail"),
    path("tickets/<int:pk>/status/", views.ticket_update_status, name="ticket-update-status"),
]
