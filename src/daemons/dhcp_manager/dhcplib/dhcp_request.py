import subprocess

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
        return " ".join(formatted)

    def __get_output(self, command, popen = False):
        if popen:
            return subprocess.Popen(self.__get_str_command(command), stdout=subprocess.PIPE, shell=True).communicate()[0]
        else:
            return subprocess.check_output(self.__get_array_command(command), shell=False)

    def __server_call(self, command):
        try:
            output = self.__get_output(command, popen = True)
        except subprocess.CalledProcessError, e:
            print "[Exception output]: %s" % (e.output,)
            raise e
        
        return output.split("\n")

    def get_leases(self):
        return self.__server_call("netsh dhcp server scope 192.168.104.0 show clients 1")

    def create_lease(self, ip, mac, name):
        return self.__server_call("netsh dhcp server scope 192.168.104.0 add reservedip %s %s '%s'" % (ip, mac, name))