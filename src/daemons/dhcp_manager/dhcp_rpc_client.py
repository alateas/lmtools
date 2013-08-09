#!/usr/bin/env python
import pika
import uuid
import leases_pb2
import requests_pb2

class DhcpRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def __do_request(self, command, *params):
        data = requests_pb2.Request()
        data.command = command
        for param in params:
            data.params.append(param)
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='lmtools_dhcp_manager_rpc',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=data.SerializeToString())
        while self.response is None:
            self.connection.process_data_events()

        return self.response.encode('utf8')

    def __parse_raw_leases(self, raw):
        pb_leases = leases_pb2.LeasesSet()
        pb_leases.ParseFromString(raw)
        return pb_leases.lease

    def __parse_raw_lease(self, raw):
        pb_lease = leases_pb2.Lease()
        pb_lease.ParseFromString(raw)
        return pb_lease

    def __parse_raw_status(self, raw):
        pb_status = leases_pb2.Status()
        pb_status.ParseFromString(raw)
        return pb_status.success

    def get_all(self):
        return self.__parse_raw_leases( self.__do_request('leases_get_all') )

    def get_range(self, ip1, ip2):
        return self.__parse_raw_leases( self.__do_request('leases_get_range', ip1, ip2) )

    def create_lease(self, ip1, ip2, mac):
        return self.__parse_raw_lease( self.__do_request('leases_create_lease', ip1, ip2, mac) )

    def delete_lease(self, ip, mac):
        return self.__parse_raw_status( self.__do_request('leases_delete_lease', ip, mac) )