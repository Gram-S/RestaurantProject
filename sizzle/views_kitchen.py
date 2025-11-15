from django.shortcuts import render, redirect
from .models import Order

def kitchen_dashboard(request):
#show pending and in progress orders, takes to the "kithen dashboard" showing these


def complete_order(request, order_id):
#mark order as complete
