#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import os

from dhcp_rpc_client import DhcpRpcClient
from leases_manager import LeasesManager

# import tornado
# from basic import require_basic_auth
# import ldapauth
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

# @require_basic_auth('Authrealm', ldapauth.auth_user_ldap)
class LeasesHandler(tornado.web.RequestHandler):
    def get(self):
        lm = LeasesManager( DhcpRpcClient().get_all() )
        self.render("leases.html", leases = lm.get_sorted_leases())

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application(
        [
            # (r"/", MainHandler),
            (r"/leases", LeasesHandler),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()