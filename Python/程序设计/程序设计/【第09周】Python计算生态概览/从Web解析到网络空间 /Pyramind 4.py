#Pyramind规模适中的web应用框架 
from wsgiref.simple_server importmake_server
from pyramid.config import Configurator
from pyramid.response import response
def hello_world(request):
    return Response('Hello World!')
if __name__ = '__main__':
    with Configurator() as config:
        config.add_route('hello','/')
        config.add_view(hello_world,route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0',6543,app)
    server.server_forever()
