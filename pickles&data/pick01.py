__author__ = 'Administrator'
import pickle

# define class
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

summer  = Bird()                 # construct an object
picklestring = pickle.dumps(summer)   # serialize object
print(picklestring)
