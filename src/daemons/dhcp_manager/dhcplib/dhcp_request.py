import subprocess
import logging

import settings
logger = logging.getLogger('dhcp_manager')

class DhcpRequest():
    def __init__(self, server, user, password):
        self.__server, self.__user, self.__password = server, user, password

    def __get_array_command(self, command):
        arr = ["cat","</dev/null", "|", "winexe", "--interactive=0", "-U", self.__user, "--password", self.__password, "//%s" % self.__server]
        arr.append("%s" % command)
        return arr
    
    def __single_quote_params(self, arr, *numbers):
        for num in numbers:
            arr[num] = "'%s'" % (arr[num],)
        
    def __get_str_command(self, command):
        formatted = self.__get_array_command(command)
        self.__single_quote_params(formatted, 8, 10)
        result = " ".join(formatted)
        if settings.debug_commands:
            logger.debug("[DhcpRequest.requestStr] " + result)
        return result

    def __get_output(self, command, popen = False):
        if popen:
            result = subprocess.Popen(self.__get_str_command(command), stdout=subprocess.PIPE, shell=True).communicate()[0]
        else:
            result =  subprocess.check_output(self.__get_array_command(command), shell=False)
        if settings.debug_output:
            logger.debug("[DhcpRequest.output] " + result)
        return result

    def __call_with_output(self, command):
        return self.__get_output(command, popen = True).split("\n")

    def __call_with_status(self, command):
        try:
            self.__get_output(command, popen = True).split("\n")
        except subprocess.CalledProcessError, e:
            return False
        return True

    def get_leases(self):
        return self.__call_with_output("netsh dhcp server scope 192.168.104.0 show clients 1")

    def create_lease(self, ip, mac, name):
        return self.__call_with_status("netsh dhcp server scope 192.168.104.0 add reservedip %s %s '%s'" % (ip, mac, name))

    def delete_lease(self, ip, mac):
        return self.__call_with_status("netsh dhcp server scope 192.168.104.0 delete reservedip %s %s" % (ip, mac))
