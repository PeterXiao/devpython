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
'''next = countdown(10)
while True:
    v = next()
    print(v)
    if not v :break'''

def coutdown2(n):
    print("Counting down from %d" %n)
    try:
        while n>0:
            yield n
            n = n-1
            print(n)
    except GeneratorExit:
        print("Only made it to %d"%n)

coutdown2(10)