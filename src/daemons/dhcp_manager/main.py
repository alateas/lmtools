# To kick off the script, run the following from the python directory:
#   PYTHONPATH=`pwd` python testdaemon.py start

#standard python libs
import logging
import time

#third party libs
from daemon import runner

#internal libs
from dhcplib.dhcp import Dhcp
from passw import info
import os

class App():
   
    def __init__(self):
        debug = True
        self.stdin_path = '/dev/null'
        if debug:
            self.stdout_path = self.stderr_path = '/dev/tty'
            # self.stderr_path = '/dev/tty'
        else:
            self.stdout_path = self.stderr_path = '/dev/null'
            # self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/lmtools_dhcp_manager.pid'
        self.pidfile_timeout = 5
        self.dhcp = Dhcp(info['server'], info['login'], info['password'])

           
    def run(self):
        while True:
            # print self.dhcp.get_range(110)
            print os.path.realpath(__file__)

            # logger.debug("Debug message")
            # logger.info("Info message")
            # logger.warn("Warning message")
            # logger.error("Error message")

            time.sleep(10)

print os.path.realpath(__file__)
app = App()
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/tmp/testdaemon.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

daemon_runner = runner.DaemonRunner(app)
#This ensures that the logger file handle does not get closed during daemonization
daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()