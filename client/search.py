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
      resp, content = h.request("http://121.199.60.181:9763/fish/rest?tag=%E7%BE%8E%E9%A3%9F&userid=23&pageSize=10&ver=1.0&format=json&type=1&pageNum=1&sign=D518ADE7C05F70AB57A25BC3ABBC9D61&timestamp=2013-12-09+15%3A38%3A39&clientid=3&session=9870CBA3BCF017844BA28DDFC1777E6A&method=com.gf.fish.gs.searching&key=1")
      print(json.loads(content)) 
    

print("done")

#print(resp)


