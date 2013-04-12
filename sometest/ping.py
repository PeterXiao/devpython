__author__ = 'Administrator'
import os
import subprocess
import subprocess
ips = "127.0.0.1"
child1 = subprocess.Popen(["ping",ips], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["cmd"], stdin=child1.stdout,stdout=subprocess.PIPE)
out = child2.communicate()
for i in out:
    if type(i):
        print(str(i.decode("gbk").encode("utf8")))
        if "TTL=" in str(i.decode("gbk").encode("utf8")):
            print("you are link to %s" % str(ips))
    else:
        print("Error")
