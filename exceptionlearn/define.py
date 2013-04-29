__author__ = 'Administrator'
#exception is object ,display about error or unusable
#handing 表示从传播机制接收异常对象，并执行所需的各种操作已处理此异常，
#try
p = lambda x:x**X
'''
try :
    statement(s)
except [expression [, target]]:
    statement(s)
[else:
    statement(s)]
#每一个except子句被称为异常处理程序（exception handler）

#异常处理可以通过sys模块的exc_info函数来获取当前异常对象
#
'''
try: 1/0
except ZeroDivisionError:print("Caught divede-by-0 attempt")
#try 的嵌套，异常传播期间将首先到达这个内部try创建的处理程序

#try/finally
'''
try:
   statement(s)
finally:
   statement(s)
#称为最终处理的必须执行的终止代码
'''
class opened(object):
    def __init__(self,filename,mode ='r'):
        self.f=open(filename,mode)
    def __enter__(self):
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
'''
#将被用作
with opened('foo.txt') as f:
#  使用已打开的文件对象f的语句
'''

