__author__ = 'Administrator'
import time

class timewith():
    def __init__(self, name=&#039;&#039;):
        self.name = name
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def checkpoint(self, name=&#039;&#039;):
        print &#039;{timer} {checkpoint} took {elapsed} seconds&#039;.format(
            timer=self.name,
            checkpoint=name,
            elapsed=self.elapsed,
        ).strip()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint(&#039;finished&#039;)
        pass

def get_number():
    for x in xrange(5000000):
        yield x

def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return &#039;some result!&#039;

# prints something like:
# fancy thing done with something took 0.582462072372 seconds
# fancy thing done with something else took 1.75355315208 seconds
# fancy thing finished took 1.7535982132 seconds
with timewith(&#039;fancy thing&#039;) as timer:
    expensive_function()
    timer.checkpoint(&#039;done with something&#039;)
    expensive_function()
    expensive_function()
    timer.checkpoint(&#039;done with something else&#039;)

# or directly
timer = timewith(&#039;fancy thing&#039;)
expensive_function()
timer.checkpoint(&#039;done with something&#039;)