# -*- coding: utf-8 -*-
import unittest
from dhcp_request import DhcpRequest
from dhcp_parser import *
from dhcp import Dhcp
from network import *
import main

class TestNetwork(unittest.TestCase):
    def test_ip_to_str(self):
        ip = Ip(192, 168, 111, 12)
        self.assertEqual(str(ip), "192.168.111.12")

    def test_ip_wrong_dgits(self):
        with self.assertRaises(InputError):
            ip = Ip(192, 168, 111, 1000)

    def test_ip_from_string(self):
        ip = Ip.from_string("192.168.104.5")
        self.assertEqual(str(ip), "192.168.104.5")

        with self.assertRaises(InputError):
            ip = Ip.from_string("192.168.256.5")

    def test_mac(self):
        mac = Mac('112233445566')
        self.assertEqual(str(mac), '112233445566')

class TestDhcpRequest(unittest.TestCase):
    def setUp(self):
        self.__request = DhcpRequest("daniel")
    
    def test_get_leases(self):
        raw_leases = self.__request.get_leases()
        self.assertTrue(raw_leases)

        ip_record_exist = False
        for line in raw_leases:
            if line.startswith("192.168.1"):
                ip_record_exist = True
        self.assertTrue(ip_record_exist)

class TestDhcpParser(unittest.TestCase):
    def test_different_leases(self):
        raw = [
        "192.168.104.1   - 255.255.248.0  -38-60-77-b4-63-f4   - ìàÄâÉÇìêùàìÄ        -U",
        "192.168.104.210 - 255.255.248.0  -99-99-99-99-99-98   - ìàÇèÆêéìÄ             -N",
        "192.168.110.17  - 255.255.248.0  - 5c-b5-24-03-f1-29   -23.06.2015 12:49:10    -D",
        ]

        parser = DhcpParser(raw)
        leases = parser.parse()

        self.assertEqual(leases[0].ip, Ip.from_string("192.168.104.1"))
        self.assertEqual(leases[1].ip, Ip.from_string("192.168.104.210"))
        self.assertEqual(leases[2].ip, Ip.from_string("192.168.110.17"))

        self.assertEqual(leases[0].mac, Mac("386077b463f4"))
        self.assertEqual(leases[1].mac, Mac("999999999998"))
        self.assertEqual(leases[2].mac, Mac("5cb52403f129"))

        self.assertIsInstance(leases[0], ReservedLease)
        self.assertIsInstance(leases[1], ReservedLease)
        self.assertIsInstance(leases[2], TemporaryLease)


class TestDhcp(unittest.TestCase):
    def setUp(self):
        self.dhcp = Dhcp()

    def test_get_range(self):
        leases = self.dhcp.get_range("104")
        for lease in leases:
            self.assertTrue(lease.ip.startswith("192.168.104."))

        leases = self.dhcp.get_range("110")
        for lease in leases:
            self.assertTrue(lease.ip.startswith("192.168.110."))

class TestRunMain(unittest.TestCase):
    def test_main_run(self):
        main.main()

if __name__ == '__main__':
    unittest.main()