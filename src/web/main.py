#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import os
# import tornado
# from basic import require_basic_auth
# import ldapauth
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

# @require_basic_auth('Authrealm', ldapauth.auth_user_ldap)
class LeasesHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("leases.html")

def main():
    static_path = '/home/alateas/lmtools/static'

    tornado.options.parse_command_line()
    application = tornado.web.Application(
        [
            # (r"/", MainHandler),
            (r"/leases", LeasesHandler),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()