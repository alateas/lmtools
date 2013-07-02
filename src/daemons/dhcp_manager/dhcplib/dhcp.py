from dhcp_parser import DhcpParser
from dhcp_request import DhcpRequest

class Dhcp():
    def __init__(self, server, user, password):
        self.__request = DhcpRequest(server, user, password)
        self.__parser = DhcpParser()

    def __get_leases(self):
        return self.__parser.parse( self.__request.get_leases() )

    def get_all(self):
        return self.__get_leases()
        
    def get_range(self, ip_start, ip_stop):
        out = []
        for lease in self.__get_leases():
            if ip_start <= lease.ip <= ip_stop:
                out.append(lease)
        return out