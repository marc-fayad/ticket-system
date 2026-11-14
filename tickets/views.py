from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Ticket


@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(requester=request.user).order_by("-pk")
    return render(request, "tickets/my_tickets.html", {"tickets": tickets})