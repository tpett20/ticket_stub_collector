from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name = 'about'),
    path('tickets/', views.tickets_index, name='index')
]