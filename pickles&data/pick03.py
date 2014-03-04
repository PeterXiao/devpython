__author__ = 'Administrator'
try:
    import cPickle as pickle
except:
    import pickle

# define the class before unpickle
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

fn     = 'a.pkl'
with open(fn, 'r') as f:
    summer = pickle.load(f)   # read file and build object


print(type(summer))