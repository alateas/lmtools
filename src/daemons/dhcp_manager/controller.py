import requests_pb2

import commands

class DhcpController(object):
    __router = {
        'leases_get_all': commands.LeasesGetAll(),
        'leases_get_range': commands.LeasesGetRange(),
    }

    def request(self, body):
        command, params = self.__parse_pb_request(body)
        if command in self.__router:
            print " [x] Request: %s %s" % (command, params,)
            return self.__router[command].call(params)
        else:
            print " [x] Unknown request: %s" % command
            return 'Unknown request'
            
    def __parse_pb_request(self, raw_request):
        pb_request = requests_pb2.Request()
        pb_request.ParseFromString(raw_request)
        cmd = pb_request.command
        params = [i for i in pb_request.params]
        return cmd, params