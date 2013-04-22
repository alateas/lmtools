from dhcplib.dhcp import Dhcp
from dhcplib.network import Ip
import leases_pb2
import requests_pb2
from passw import info

class DhcpModel(object):
    def __init__(self):
        self.__dhcp = Dhcp(info['server'], info['login'], info['password'])

    def get_leases_by_range(self, ip1, ip2):
        return self.__dhcp.get_range(Ip.from_string(ip1), Ip.from_string(ip2))

    def get_pb_leases_by_range(self, ip1, ip2):
        leases = self.get_leases_by_range(ip1, ip2)
        pb_leases = leases_pb2.LeasesSet()
        for lease in leases:
            pb_lease = pb_leases.lease.add()
            
            pb_lease.name = lease.name
            pb_lease.ip   = str(lease.ip)
            pb_lease.mac  = str(lease.mac)

        return pb_leases.SerializeToString()

    def get_ip_range_from_pb(self, pb_range_request):
        pb_request = requests_pb2.IpRangeRequest()
        pb_request.ParseFromString(pb_range_request)
        return (pb_request.ip1, pb_request.ip2)