from dhcp_parser import DhcpParser
from dhcp_request import DhcpRequest

class Dhcp():
    def __init__(self):
        request = DhcpRequest("daniel")
        raw_leases = request.get_leases()

        log_file = open("out.txt","w")
        for line in raw_leases:
            log_file.write(str(line) + "\n")
        log_file.close()


        parser = DhcpParser(raw_leases)
        self.leases = parser.parse()

    def get_range(self, range_nummber):
        out = []
        for lease in self.leases:
            if lease.ip.num1==192 and lease.ip.num2==168 and lease.ip.num3==range_nummber:
                out.append(lease)
        return out