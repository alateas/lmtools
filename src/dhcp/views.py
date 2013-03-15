# Create your views here.
from django.shortcuts import render

def test(request):
    return render(request, 'dhcp/leases.html')
