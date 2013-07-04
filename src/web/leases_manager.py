import socket

class LeasesManager(object):
    __ranges = {
        'thin_clients'    : ('192.168.104.1',   '192.168.104.199'),
        'machine'         : ('192.168.104.200', '192.168.104.255'),
        'ip_cameras'      : ('192.168.105.1',   '192.168.105.255'),
        'temp_servers'    : ('192.168.106.1',   '192.168.106.255'),
        'computers'       : ('192.168.107.1',   '192.168.107.255'),
        'personal_unlim'  : ('192.168.108.1',   '192.168.108.99'),
        'personal_others' : ('192.168.108.100', '192.168.108.255'),
        'ip_phones'       : ('192.168.109.1',   '192.168.109.199'),
        'printers'        : ('192.168.109.200', '192.168.109.255'),
        'temp'            : ('192.168.110.1',   '192.168.110.255'),
        'servers'         : ('192.168.111.1',   '192.168.111.255'),
    }

    def get_ips_by_range_name(self, range_name):
        return self.__ranges[range_name][0], self.__ranges[range_name][1]

    def get_sorted_leases(self, raw_leases):

        sorted_leases = dict([key, []] for key, ip_range in self.__ranges.iteritems())
        for lease in raw_leases:
            if not lease.name:
                lease.name = "-"
            sorted_leases[self.__get_range(lease)].append(lease)
        return sorted_leases

    def __get_range(self, lease):
        for key, ip_range in self.__ranges.iteritems():
            if self.__in_range(lease, ip_range):
                return key
        return None

    def __in_range(self, lease, ip_range):
        ip = socket.inet_aton(lease.ip)
        ip_start = socket.inet_aton(ip_range[0])
        ip_end = socket.inet_aton(ip_range[1])
        
        return (ip>=ip_start) and (ip<=ip_end)