from django.shortcuts import render_to_response
from dhcplib.dhcp import Dhcp
from django.conf import settings

def list(request):
    user = settings.PASSWORDS['autoadmin'][0]
    password = settings.PASSWORDS['autoadmin'][1]

    dhcp = Dhcp("daniel", user, password)
    leases = dhcp.get_range(110)
    return render_to_response('dhcp/leases.html', {'leases': leases})