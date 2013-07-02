from dhcp_parser import DhcpParser
from dhcp_request import DhcpRequest
from network import Ip

class Dhcp():
    def __init__(self, server, user, password):
        self.__request = DhcpRequest(server, user, password)
        self.__parser = DhcpParser()
        self.__leases = self.__parser.parse( self.__request.get_leases() )

    def get_all(self):
        return self.__leases
        
    def get_range(self, ip_start, ip_stop):
        if ip_start.num1 != ip_stop.num1 or ip_start.num2 != ip_stop.num2 or ip_start.num3 != ip_stop.num3:
            raise AssertionError

        out = []
        for lease in self.get_all():
            if ip_start <= lease.ip <= ip_stop:
                out.append(lease)
        return out

    def __get_lease_by_mac(self, mac):
        leases = self.get_all()
        for lease in leases:
            if lease.mac == mac:
                return lease
        return None
    
    def __get_first_free_ip(self, ip_start, ip_stop):
        leases = self.get_range(ip_start, ip_stop)
        last_nums = map(lambda lease:lease.ip.num4, leases)
        full_range = range(ip_start.num4, ip_stop.num4+1)
        for i in full_range:
            if i not in last_nums:
                return Ip(ip_start.num1, ip_start.num2, ip_start.num3, i)

        return None

    def create_lease_in_range(self, ip_start, ip_stop, mac):
        lease = self.__get_lease_by_mac(mac)
        ip = self.__get_first_free_ip(ip_start, ip_stop)
        if lease and ip:
            self.__request.create_lease(ip, mac, lease.name)
            return ip
        return None
