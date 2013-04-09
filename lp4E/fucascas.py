__author__ = 'Administrator'
'''def callf(func):
    return func()
def helloworld():
    print( "hello world")
callf(helloworld())'''
def countdown(n):
    def next():
        nonlocal n
        r = n
        n -=1
        return
    return next
#test
next = countdown(10)
while True:
    v = next()
    print(v)
    if not v :break