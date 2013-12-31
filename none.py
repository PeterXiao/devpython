android 渠道号激活，
php with vm
java
go
python jswithwebandnode
#!/usr/bin/env python
#coding=utf-8
def opensa():
	f = open('a.txt','r')
	result = list()
	for line in f.readlines():
			line = line.strip()
			if not len(line) or line.startswith('#'):
					continue
			result.append(line)
	result.sort()
	print result
	
#!/usr/bin/env python
#coding=utf-8
file = open("key.txt","r")
buf = file.readlines()
file.close()
result = {}
for line in buf:
        left,right = line.split()
#       print left,right
        if result.has_key(right):
                result[right].append(left)
#               print result
        else:
                result[right] = [left]
print result



from collections import Counter
import re

class pulicts:
        def __init__(self,filename):
                self.openfile = open(filename,'r')
                self.all_list = []
                self.all_time = {}
                self.dicts = {}
		self.rg = re.compile(
							r'^(?:\d+\.){3}\d+\,\s[^\s]+\s\-\s\-\s'
							+ r'\[[^\[\]]+\]\s{2}'
							+ r'\"([^\"]+)\"'
							+ r'\s{2}\d+\s\d+\s{2}'
							+ r'\"[^\"]+\"\s{2}'
							+ r'\"[^\"]+\"\s'
							+ r'(\d+\.\d+)'
							)
class Database(pulicts):
        def __init__(self,filename):
                pulicts.__init__(self,filename)
        def start(self):
                for i in self.openfile:
                        m = self.rg.search(i)
                        if m:
                                urls = m.group(1)
                                times = m.group(2)
                                print urls
                                self.all_list.append(urls)
                                ti = "%.4f" % float(times)
                                if self.all_time.get(urls) == None:
                                        self.all_time[urls]= ti
                                else:
                                        a = float(self.all_time.get(urls)) + float(ti)
                                        self.all_time[urls] = a
        def lists(self):
                c = Counter(self.all_list)
                list_first_10 = c.most_common(10)
                for i in range(len(list_first_10)):
                        a =list_first_10[i][1]
                        e = list_first_10[i][0]
                        b = self.all_time.get(e)
                        times = float(b)/float(a)
                        self.dicts[e] = "%.4f" % times
                print self.dicts
starts = Database('/home/www/biglog')
starts.start()
starts.lists()
#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from eventlet import api
def httpd(writer,reader):
    req=''
    while True:
        chunk=reader.readline()
        if not chunk:
            break
        req+=chunk
        if chunk=='\r\n':
            break
    data='Hello world!\r\n'
    writer.write('HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s'%(len(data),data))
    writer.close()
    reader.close()
    return
def main():
    try:
        server=api.tcp_listener(('0.0.0.0',3000))
        print 'Server started!'
        while True:
            conn,addr=server.accept()
            #print 'client %s connected!'%repr(addr)
            writer=conn.makefile('w')
            api.spawn(httpd,writer,conn.makefile('r'))
    except KeyboardInterrupt:
        pass
    return
	
	
  import re
def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()
 
def txt_wrap_by_all(start_str, end, html):
   result = []
   from_pos = 0
   while True:
       start = html.find(start_str, from_pos)
       if start >= 0:
           start += len(start_str)
           endpos = html.find(end, start)
           if endpos >= 0:
               result.append(html[start:endpos].strip())
               from_pos = endpos+len(end)
               continue
       break
   return result
 
 
def strip_txt_wrap_by(start, end, html):
   t = txt_wrap_by(start, end, html)
   if t:
       return strip_line(t)
 
 
def strip_line(txt):
   txt = txt.replace("　", " ").split("\n")
   return "\n".join(i for i in [i.strip() for i in txt] if i)
if __name__=='__main__':
    main()
	
	
	

