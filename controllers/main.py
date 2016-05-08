import os

import tornado
from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

from modules import uimodules

rootdirectorypath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ))

class LandingHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.redirect("/main")


class MainHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render(rootdirectorypath+"/templates/main.html")


class ApiHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self):
        pass


def run(port):
    settings = {
        "ui_modules": uimodules
    }
    app = Application([(r"/api", ApiHandler),
                       (r"/main", MainHandler),
                       (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": rootdirectorypath+"/static/"}),
                       (r"/models/(.*)", tornado.web.StaticFileHandler, {"path": rootdirectorypath+"/models/"}),
                       (r"/(.*)", LandingHandler)],
                      autoreload=True, **settings)
    server = HTTPServer(app)
    server.listen(port)
    print 'Radient running at ' + port
    tornado.ioloop.IOLoop.current().start()
