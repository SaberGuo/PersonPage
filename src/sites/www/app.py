#coding=utf-8
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options
tornado.options.parse_command_line()

define('port', default = 8080, type = int, help = 'app listen port')


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('index.html')


def create_app():
    settings = {
        'static_path': 'src/sites/www/static',
        'template_path': 'src/sites/www/templates',
        'debug': True,
    }

    handlers = [
        (r"/", HomeHandler),
    ]

    return tornado.web.Application(handlers, **settings)

if __name__=="__main__":
    app = create_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()