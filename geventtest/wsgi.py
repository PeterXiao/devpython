__author__ = 'Administrator'
from gevent.wsgi import WSGIServer


def application(environ, start_response):
    status = '200 OK'
    body = '<p>Hello World</p>'



    headers = [
        ('Content-Type', 'text/html')
    ]



    start_response(status, headers)
    return [body]



#WSGIServer(('', 8000), application).serve_forever()
from paste import httpserver
httpserver.serve(application, '0.0.0.0', request_queue_size=500)