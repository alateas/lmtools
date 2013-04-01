import subprocess
from django.conf import settings

class DhcpRequest():
    def __init__(self, server):
        self.__server = server

    def __server_call(self, command):
        user = settings.PASSWORDS['autoadmin'][0]
        password = settings.PASSWORDS['autoadmin'][1]
        prefix = ["winexe", "-U", user, "--password=%s" % password, "//%s" % self.__server]
        # result_cmd = "%s \"%s\"" % (prefix, command)
        prefix.append(command)
        print prefix
        output = subprocess.check_output(prefix)
        return output.split("\n")

    def get_leases(self):
        return self.__server_call("netsh dhcp server scope 192.168.104.0 show clients 0")
        # return self.__server_call(["netsh", "dhcp", "server", "scope", "192.168.104.0", "show", "clients", "0"])        