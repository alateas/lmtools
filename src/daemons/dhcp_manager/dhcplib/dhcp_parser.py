import re
import network
def lease_factory(type):
    if(type=='D'):
        return TemporaryLease
    else:
        return ReservedLease

class Lease():
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac

    def __str__(self):
        return "%s [%s]" % (self.ip, self.mac)

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
        for line in self.__raw:
            regular = re.compile('\d{2}\.\d{2}.\d{4}\s\d{1,2}:\d{2}:\d{2}')
            if(line.startswith("192.168.1")):
                date = False
                searched = regular.search(line)
                if searched:
                    date = line[searched.span()[0]:searched.span()[1]]
                    line = line[:searched.span()[0]]+ line[searched.span()[1]:]

                s = " ".join(line.split()).replace("-", "").split(" ")
                s.remove("")
                s.remove("")
                s.pop(len(s)-2)
                reserved = bool()
                ip = network.Ip.from_string(s[0])
                mac = network.Mac(s[2])
                lease = lease_factory(s[-1])(ip, mac)
                if(date):
                    lease.set_date(date)
                self.leases.append(lease);
                #endif
        return self.leases
