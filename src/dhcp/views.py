from django.shortcuts import render_to_response
from dhcplib.dhcp import Dhcp

def list(request):
    dhcp = Dhcp()
    leases = dhcp.get_range(110)
    return render_to_response('dhcp/leases.html', {'leases': leases})