__author__ = 'Administrator'
'''
使用subprocess包中的函数创建子进程的时候，要注意:

1) 在创建子进程之后，父进程是否暂停，并等待子进程运行。

2) 函数返回什么

3) 当returncode不为0时，父进程如何处理。
subprocess包中定义有数个创建子进程的函数，
这些函数分别以不同的方式创建子进程，
所以我们可以根据需要来从中选取一个使用。
另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，
从而在进程间使用文本通信。
'''

import subprocess
try:
   rc = subprocess.call(["ls","-l"])
except WindowsError:
    rc =subprocess.call(["ipconfig","/all"])

import subprocess
child = subprocess.Popen(["ping","-c","5","www.google.com"])
print("parent process")
"""
child.poll()           # 检查子进程状态

child.kill()           # 终止子进程

child.send_signal()    # 向子进程发送信号

child.terminate()      # 终止子进程

子进程的PID存储在child.pid
"""
import subprocess
child = subprocess.Popen(["ping","-c","5","www.google.com"])
child.wait()
print("parent process")

import subprocess
child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE)
out = child2.communicate()
print(out)


import subprocess
child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
child.communicate("vamei")

"""
通过使用subprocess包，我们可以运行外部程序。
这极大的拓展了Python的功能。如果你已经了解了操作系统的某些应用，
你可以从Python中直接调用该应用(而不是完全依赖Python)，
并将应用的结果输出给Python，并让Python继续处理。
shell的功能(比如利用文本流连接各个应用)，就可以在Python中实现。
"""