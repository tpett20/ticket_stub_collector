from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ticket

# Create your views here.
def about(request):
    return render(request, 'about.html')

def tickets_index(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/index.html', {
        'tickets': tickets
    })

def tickets_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'tickets/detail.html', {
        'ticket': ticket
    })

class TicketCreate(CreateView):
    model = Ticket
    fields = '__all__'

class TicketUpdate(UpdateView):
    model = Ticket
    fields = '__all__'

class TicketDelete(DeleteView):
    model = Ticket
    success_url = '/tickets'