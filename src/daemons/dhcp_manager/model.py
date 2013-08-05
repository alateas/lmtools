from dhcplib.dhcp import Dhcp
from dhcplib.network import Ip, Mac
from passw import info

import leases_pb2

class DhcpModel(object):
    def __init__(self):
        self.__dhcp = Dhcp(info['server'], info['login'], info['password'])

    def __get_leases_by_range(self, ip1, ip2):
        return self.__dhcp.get_range(Ip.from_string(ip1), Ip.from_string(ip2))

    def __get_all_leases(self):
        return self.__dhcp.get_all()

    def __create_lease(self, ip1, ip2, mac):
        return self.__dhcp.create_lease_in_range(Ip.from_string(ip1), Ip.from_string(ip2), Mac(mac))

    def __delete_lease(self, ip):
        return self.__dhcp.delete_lease(Ip.from_string(ip))

    def get_pb_leases_by_range(self, ip1, ip2):
        return self.__wrap_leases_to_pb( self.__get_leases_by_range(ip1, ip2) )

    def get_pb_all_leases(self):
        return self.__wrap_leases_to_pb( self.__get_all_leases() )

    def pb_create_lease(self, ip1, ip2, mac):
        return self.__wrap_lease_to_pb( self.__create_lease(ip1, ip2, mac) )

    def pb_delete_lease(self, ip):
        return self.__wrap_status_to_pb(self.__delete_lease(ip))

    def __wrap_status_to_pb(self, status):
        pb_status = leases_pb2.Status()
        pb_status.success = status
        return pb_status.SerializeToString()

    def __wrap_lease_to_pb(self, lease):
        pb_lease = leases_pb2.Lease()
        pb_lease.name = lease.name
        pb_lease.ip   = str(lease.ip)
        pb_lease.mac  = str(lease.mac)

        return pb_lease.SerializeToString()

    def __wrap_leases_to_pb(self, leases):
        pb_leases = leases_pb2.LeasesSet()
        for lease in leases:
            pb_lease = pb_leases.lease.add()
            pb_lease.name = lease.name
            pb_lease.ip   = str(lease.ip)
            pb_lease.mac  = str(lease.mac)

        return pb_leases.SerializeToString()