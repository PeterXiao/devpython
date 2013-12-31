__author__ = 'Administrator'
import time

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, &#039;took&#039;, end - start, &#039;time&#039;
        return result
    return f_timer

def get_number():
    for x in xrange(5000000):
        yield x

@timefunc
def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return &#039;some result!&#039;

# prints "expensive_function took 0.72583088875 seconds"
result = expensive_function()