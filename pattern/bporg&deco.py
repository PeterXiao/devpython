__author__ = 'Administrator'
def borg(cls):
    cls._state = {}
    orig_init = cls.__init__
    def new_init(self, *args, **kwargs):
        self.__dict__ = cls._state
        orig_init(self, *args, **kwargs)
    cls.__init__ = new_init
    return cls

@borg
class TestBorg(object):
    def say_borg(self):
        print "i am borg"


if __name__ =='__main__':
    test = TestBorg(borg)
    test.say_borg()