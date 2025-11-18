from django.shortcuts import render
from .models import computer

def computer_list(request):
    computers = computer.objects.all()
    return render(request, 'computer_list.html', {'computers': computers})