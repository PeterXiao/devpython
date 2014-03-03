'''
Created on 2013-12-9

@author: Administrator
'''
import httplib2,base64
import simplejson as json

def WorkArray():
    
    pass

def Responseofsearch(object):
    if type(object) == 'json':
        print("pass") 
    pass

h = httplib2.Http()
for i in range(10):
      resp, content = h.request("http://192.168.3.223:9763/fish/rest?clientid=3&timestamp=2014-02-28+09%3A54%3A50&sign=C6709A94107A6350881BCD4229049552&workid=15&session=9870CBA3BCF017844BA28DDFC1777E6A&userid=23&method=com.gf.fish.gs.likeDislike&format=json&ver=1.0&type=2")
      print(json.loads(content)) 
    

print("done")

#print(resp)


