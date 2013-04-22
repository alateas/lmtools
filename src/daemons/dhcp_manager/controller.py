from model import DhcpModel

class DhcpController(object):
    def __init__(self):
        self.__model = DhcpModel()

    def request(self, body):
        ip1, ip2 = self.__model.get_ip_range_from_pb(body)
        print " [x] Request: %s %s" % (ip1, ip2,)
        print "leases : %s" % (self.__model.get_pb_leases_by_range(ip1, ip2),)
        return str(self.__model.get_pb_leases_by_range(ip1, ip2))
