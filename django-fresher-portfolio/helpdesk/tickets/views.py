from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import TicketForm
from .models import Ticket


@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    status = request.GET.get("status", "")
    if status in Ticket.Status.values:
        tickets = tickets.filter(status=status)
    return render(request, "tickets/list.html", {"tickets": tickets, "selected_status": status})


@login_required
def ticket_create(request):
    form = TicketForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        ticket = form.save(commit=False)
        ticket.created_by = request.user
        ticket.save()
        return redirect("ticket-detail", pk=ticket.pk)
    return render(request, "tickets/form.html", {"form": form})


@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, created_by=request.user)
    return render(request, "tickets/detail.html", {"ticket": ticket})


@login_required
@require_POST
def ticket_update_status(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, created_by=request.user)
    status = request.POST.get("status")
    if status in Ticket.Status.values:
        ticket.status = status
        ticket.save(update_fields=["status", "updated_at"])
    return redirect("ticket-detail", pk=ticket.pk)
