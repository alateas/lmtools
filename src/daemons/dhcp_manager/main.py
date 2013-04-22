# To kick off the script, run the following from the python directory:
#   PYTHONPATH=`pwd` python testdaemon.py start

#standard python libs
import logging
import time
import os

#third party libs
from daemon import runner
import pika

#internal libs
# from model import DhcpModel
import controller

class App():
    def __init_log(self):
        self.__logger = logging.getLogger("dhcp_manager")
        self.__logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.handler = logging.FileHandler("/var/log/lmtools/dhcp_manager.log")
        self.handler.setFormatter(formatter)
        self.__logger.addHandler(self.handler)

    def __init_mq(self):
        self.__connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.__channel = self.__connection.channel()
        self.__channel.queue_declare(queue='lmtools_dhcp_manager_rpc')
    
    def __init__(self):
        self.__init_log()

        self.__controller = controller.DhcpController()

        debug = True
        self.stdin_path = '/dev/null'
        if debug:
            self.stdout_path = self.stderr_path = '/dev/tty'
        else:
            self.stdout_path = self.stderr_path = '/dev/null'

        self.pidfile_path = '/tmp/lmtools/dhcp_manager.pid'
        self.pidfile_timeout = 5
        
           
    def on_request(self, ch, method, props, body):
        self.__logger.info("request: %s" % (body,))
        
        response = self.__controller.request(body)
        # ip1, ip2 = self.__model.get_ip_range_from_pb(body)
        # print " [x] Request: %s %s" % (ip1, ip2,)
        # response = self.__model.get_pb_leases_by_range(ip1, ip2)
        ch.basic_publish(exchange='', 
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id = props.correlation_id),
                         body=response)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    def run(self):
        self.__init_mq()
        self.__channel.basic_qos(prefetch_count=1)
        self.__channel.basic_consume(self.on_request, queue='lmtools_dhcp_manager_rpc')

        print " [x] Awaiting RPC requests"
        self.__channel.start_consuming()
        # self.__logger.error("Error message")

print os.path.realpath(__file__)
app = App()
daemon_runner = runner.DaemonRunner(app)
#This ensures that the logger file handle does not get closed during daemonization
daemon_runner.daemon_context.files_preserve=[app.handler.stream]
daemon_runner.do_action()