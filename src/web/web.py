#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import os
import json

from basic import require_basic_auth
import ldapauth
from dhcp_rpc_client import DhcpRpcClient
from leases_manager import LeasesManager

from tornado.options import define, options, parse_command_line
from logger import log_path

define("port", default=8888, help="run on the given port", type=int)
tornado.options.options.log_file_prefix = os.path.join(log_path, "web.log")
tornado.options.parse_command_line()

lm = LeasesManager()

@require_basic_auth('AuthRealm', ldapauth.auth_user_ldap)
class LeasesHandler(tornado.web.RequestHandler):
    def get(self):
        
        self.render("leases.html", leases = lm.get_sorted_leases(DhcpRpcClient().get_all()))

@require_basic_auth('AuthRealm', ldapauth.auth_user_ldap)
class CreateLease(tornado.web.RequestHandler):
    def post(self):
        dest_range, mac = self.get_argument('dest_range'), self.get_argument('mac')
        ip1, ip2 = lm.get_ips_by_range_name(dest_range)
        lease = DhcpRpcClient().create_lease(ip1, ip2, mac)
        if lease:
            response = {'status':'OK', 'ip': lease.ip, 'name':lease.name}
        else:
            response = {'status':'ERROR'}

        self.write(response)

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application(
        [
            (r"/", tornado.web.RedirectHandler, {"url": "/leases"}),
            (r"/leases", LeasesHandler),
            (r"/ajax/create_lease", CreateLease),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), "static")}),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()