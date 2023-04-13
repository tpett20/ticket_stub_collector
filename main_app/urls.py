from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name = 'about'),
    path('tickets/', views.tickets_index, name='index'), 
    path('tickets/<int:ticket_id>/', views.tickets_detail, name='detail'),
    path('tickets/create/', views.TicketCreate.as_view(), name='tickets_create')
]