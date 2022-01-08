import os
import tornado.ioloop
import tornado.web
import config

root = os.path.dirname(__file__)
port = config.port
name = config.name


application = tornado.web.Application([
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"})
])

if __name__ == '__main__':
    application.listen(port)
    print(f'{name} has been started on port {port}')
    tornado.ioloop.IOLoop.instance().start()