__author__ = 'Administrator'
class ConnectionSingleton(object):
    '''通过重载实例化函数__new__缓存mongodb连接'''
    conn=None
    def __new__(cls,*args,**kwds):
        if cls.conn is None:
            cls.conn=pymongo.MongoClient()
        return cls.conn

db = ConnectionSingleton()