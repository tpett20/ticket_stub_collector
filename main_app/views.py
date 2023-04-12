from django.shortcuts import render
from .models import Ticket

# tickets = [
#     {'event': 'Mets v. Phillies', 'date': '4/29/2022', 'venue': 'Citi Field, NY', 'highlight': 'First Combined No-Hitter in Mets Franchise History!'},
#     {'event': 'Mets v. Marlins', 'date': '9/28/2022', 'venue': 'Citi Field, NY', 'highlight': 'Eduardo Escobar Walk-Off Single (and 2-Run HR)!'}, 
#     {'event': 'Rays v. Royals', 'date': '8/20/2018', 'venue': 'Tropicana Field, FL', 'highlight': 'Ji-Man Choi Bunt Single Against the Shift'}
# ]

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