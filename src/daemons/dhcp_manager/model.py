from dhcplib.dhcp import Dhcp
from dhcplib.network import Ip
from passw import info

import leases_pb2

class DhcpModel(object):
    def __init__(self):
        self.__dhcp = Dhcp(info['server'], info['login'], info['password'])

    def __get_leases_by_range(self, ip1, ip2):
        return self.__dhcp.get_range(Ip.from_string(ip1), Ip.from_string(ip2))

    def __get_all_leases(self):
        return self.__dhcp.get_all()

    def get_pb_leases_by_range(self, ip1, ip2):
        leases = self.__get_leases_by_range(ip1, ip2)
        return self.__wrap_leases_to_pb(leases)

    def get_pb_all_leases(self):
        leases = self.__get_all_leases()
        return self.__wrap_leases_to_pb(leases)

    def __wrap_leases_to_pb(self, leases):
        pb_leases = leases_pb2.LeasesSet()
        for lease in leases:
            pb_lease = pb_leases.lease.add()
            pb_lease.name = lease.name
            pb_lease.ip   = str(lease.ip)
            pb_lease.mac  = str(lease.mac)

        return pb_leases.SerializeToString()