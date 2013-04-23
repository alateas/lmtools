from model import DhcpModel

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

    def __get_pb_leases_by_range(self, ip1, ip2):
        return self.__model.get_pb_leases_by_range(ip1, ip2)

    def __get_pb_all_leases(self):
        return self.__model.get_pb_all_leases()