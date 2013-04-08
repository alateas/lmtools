import subprocess

class DhcpRequest():
    def __init__(self, server, user, password):
        self.__server, self.__user, self.__password = server, user, password

    def __server_call(self, command):
        prefix = ["winexe", "-U", self.__user, "--password=\"%s\"" % self.__password, "//%s" % self.__server]
        # result_cmd = "%s \"%s\"" % (prefix, command)
        prefix.append("\"%s\"" % command)
        final = " ".join(prefix)
        output = subprocess.Popen(final, stdout=subprocess.PIPE, shell=True).communicate()[0]
        return output.split("\n")

    def get_leases(self):
        return self.__server_call("netsh dhcp server scope 192.168.104.0 show clients 0")
        # return self.__server_call(["netsh", "dhcp", "server", "scope", "192.168.104.0", "show", "clients", "0"])        