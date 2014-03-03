__author__ = 'Administrator'
from gevent.wsgi import WSGIServer


def application(environ, start_response):
    status = '200 OK' #页面状态指定为200 ok
    body = '<p>Hello World</p>'



    headers = [
        ('Content-Type', 'text/html')
    ]



    start_response(status, headers)
    return [body]



WSGIServer(('', 8000), application).serve_forever() #启动一个占用8000端口的wsgi服务器