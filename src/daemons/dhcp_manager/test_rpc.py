import leases_pb2

from dhcp_rpc_client import DhcpRpcClient

client = DhcpRpcClient()

# for lease in client.get_range('192.168.104.0', '192.168.104.255'):
    # print "%s %s %s" % (lease.name, lease.ip, lease.mac, )

# for lease in client.get_all():
    # print "%s %s %s" % (lease.name, lease.ip, lease.mac, )

print client.delete_lease('192.168.106.14')