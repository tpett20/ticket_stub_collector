from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ticket
from .forms import CommentForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tickets_index(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/index.html', {
        'tickets': tickets
    })

def tickets_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    comment_form = CommentForm()
    return render(request, 'tickets/detail.html', {
        'ticket': ticket,
        'comment_form': comment_form
    })

def add_comment(request, ticket_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.ticket_id = ticket_id
        new_comment.save()
    return redirect('detail', ticket_id=ticket_id)

class TicketCreate(CreateView):
    model = Ticket
    fields = '__all__'

class TicketUpdate(UpdateView):
    model = Ticket
    fields = '__all__'

class TicketDelete(DeleteView):
    model = Ticket
    success_url = '/tickets'