from model import DhcpModel

import leases_pb2
import requests_pb2


class DhcpController(object):
    def __init__(self):
        self.__model = DhcpModel()

    def request(self, body):
        ip1, ip2 = self.__get_ip_range_from_pb(body)
        print " [x] Request: %s %s" % (ip1, ip2,)
        return self.__get_pb_leases_by_range(ip1, ip2)

    def __get_ip_range_from_pb(self, pb_range_request):
        pb_request = requests_pb2.IpRangeRequest()
        pb_request.ParseFromString(pb_range_request)
        return (pb_request.ip1, pb_request.ip2)

    def __wrap_leases_to_pb(self, leases):
        pb_leases = leases_pb2.LeasesSet()
        for lease in leases:
            pb_lease = pb_leases.lease.add()
            pb_lease.name = lease.name
            pb_lease.ip   = str(lease.ip)
            pb_lease.mac  = str(lease.mac)

        return pb_leases.SerializeToString()

    def __get_pb_leases_by_range(self, ip1, ip2):
        leases = self.__model.get_leases_by_range(ip1, ip2)
        return self.__wrap_leases_to_pb(leases)

    def __get_pb_all_leases(self):
        leases = self.__model.get_all_leases()
        return self.__wrap_leases_to_pb(leases)    