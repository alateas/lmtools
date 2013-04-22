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

    def get_range(self, ip1, ip2):
        data = requests_pb2.IpRangeRequest()
        data.ip1, data.ip2 = ip1, ip2
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
        
        pb_leases = leases_pb2.LeasesSet()
        pb_leases.ParseFromString(self.response.encode('utf8'))
        return pb_leases.lease