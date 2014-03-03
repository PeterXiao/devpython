__author__ = 'Administrator'
from gevent.pywsgi import WSGIServer #使用pywsgi可以我们自己定义产生结果的处理引擎


def application(environ, start_response):
    status = '200 OK'



    headers = [
        ('Content-Type', 'text/html')
    ]



    start_response(status, headers)
    yield "<p>Hello" #yield出数据
    yield "World</p>"



WSGIServer(('', 8000), application).serve_forever()