from dhcp_parser import DhcpParser
from dhcp_request import DhcpRequest

class Dhcp():
    def __init__(self, server, user, password):
        request = DhcpRequest(server, user, password)
        raw_leases = request.get_leases()

        # log_file = open("out.txt","w")
        # for line in raw_leases:
            # log_file.write(str(line) + "\n")
        # log_file.close()

        parser = DhcpParser(raw_leases)
        self.leases = parser.parse()

    def get_range(self, ip_start, ip_stop):
        out = []
        for lease in self.leases:
            if (lease.ip > ip_start) and (lease.ip < ip_stop):
                print lease
                out.append(lease)
        return out