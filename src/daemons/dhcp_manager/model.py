from dhcplib.dhcp import Dhcp
from dhcplib.network import Ip
from passw import info

class DhcpModel(object):
    def __init__(self):
        self.__dhcp = Dhcp(info['server'], info['login'], info['password'])

    def get_leases_by_range(self, ip1, ip2):
        return self.__dhcp.get_range(Ip.from_string(ip1), Ip.from_string(ip2))

    def get_all_leases(self):
        return self.__dhcp.get_all()