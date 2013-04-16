import socket, struct

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class Ip():
    def __init__(self, num1, num2, num3, num4):
        self.__validate_numbers((num1, num2, num3, num4))
        self.num1, self.num2, self.num3, self.num4  = num1, num2, num3, num4

    @classmethod
    def from_string(self, str):
        args = map(lambda x: int(x), str.strip().split('.'))
        return Ip(*args)

    def __validate_numbers(self, numbers):
        for num in numbers:
            if num < 0 or num > 255:
                raise InputError('ip class creation', 'ip numbers can\'t be negetive or grather than 255')

    def __gt__(self, ip2):
        return socket.inet_aton(str(self)) > socket.inet_aton(str(ip2))

    def __lt__(self, ip2):
        return socket.inet_aton(str(self)) < socket.inet_aton(str(ip2))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "%s.%s.%s.%s" % (self.num1, self.num2, self.num3, self.num4)

    def __repr__(self):
        return "%s(%s)" % ( self.__class__, self.__str__() )      

class Mac():
    def __init__(self, mac):
        self.__mac = mac

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return self.__mac

    def __repr__(self):
        return "%s(%s)" % ( self.__class__, self.__str__() )