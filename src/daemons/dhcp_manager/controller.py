import requests_pb2

import commands
import logging

logger = logging.getLogger('dhcp_manager')

class DhcpController(object):
    __router = {
        'leases_get_all': commands.LeasesGetAll(),
        'leases_get_range': commands.LeasesGetRange(),
        'leases_create_lease': commands.CreateLease(),
        'leases_delete_lease': commands.DeleteLease(),
    }

    def request(self, body):
        command, params = self.__parse_pb_request(body)
        if command in self.__router:
            logger.info("[x] Request: %s %s" % (command, params,))
            return self.__router[command].call(params)
        else:
            logger.info("[x] Unknown request: %s" % command)
            return 'Unknown request'
            
    def __parse_pb_request(self, raw_request):
        pb_request = requests_pb2.Request()
        pb_request.ParseFromString(raw_request)
        cmd = pb_request.command
        params = [i for i in pb_request.params]
        return cmd, params