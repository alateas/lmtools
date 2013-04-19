# -*- coding: utf-8 -*- 

import re
import network

def lease_factory(type):
    if(type=='D'):
        return TemporaryLease
    else:
        return ReservedLease

class Lease():
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name

    def __str__(self):
        return "{%s} %s [%s]" % (self.name, self.ip, self.mac)

    def __repr__(self):
        return "%s(%s)" % ( self.__class__, self.__str__() )

class ReservedLease(Lease):
    pass

class TemporaryLease(Lease):
    def __init__(self, *args, **kw): 
        Lease.__init__(self, *args, **kw)
        self.__date="-"

    def set_date(self, date):
        self.__date = date
    def __str__(self):
        return "%s TEMP" % Lease.__str__(self)

class DhcpParser():
    def __init__(self, raw):
        self.__raw = raw

    def parse(self):
        self.leases = []
        date_regexp = re.compile('(\d{2}\.\d{2}.\d{4}\s\d{1,2}:\d{2}:\d{2})')
        name_regexp = re.compile('(-(D|U|N|R)-){1}\s*(.*)')
        for line in self.__raw:
            if(line.startswith("192.168")):
                searched_name = name_regexp.search(line)
                name = searched_name.groups()[2].decode('cp866').rstrip('\r')
                line = line[:searched_name.start(3)]
                date = False
                searched_date = date_regexp.search(line)
                if searched_date:
                    date = line[searched_date.span()[0]:searched_date.span()[1]]
                    line = line[:searched_date.span()[0]]+ line[searched_date.span()[1]:]

                s = " ".join(line.split()).replace("-", "").split(" ")
                s.remove("")
                s.remove("")
                ip = network.Ip.from_string(s[0])
                mac = network.Mac(s[2])
                lease = lease_factory(s[-1])(ip, mac, name)
                if(date):
                    lease.set_date(date)
                self.leases.append(lease);
                #endif
        return self.leases
