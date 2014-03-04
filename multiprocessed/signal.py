__author__ = 'Administrator'
'''
signal包的核心是使用signal.signal()函数来预设(register)信号处理函数，如下所示：

singnal.signal(signalnum, handler)

signalnum为某个信号，handler为该信号的处理函数。
我们在信号基础里提到，进程可以无视信号，可以采取默认操作，
还可以自定义操作。当handler为signal.SIG_IGN时，信号被无视(ignore)。
当handler为singal.SIG_DFL，进程采取默认操作(default)。当handler为一个函数名时，
进程采取函数中定义的操作。
'''

import signal
# Define signal handler function
def myHandler(signum, frame):
    print('I received: ', signum)

# register signal.SIGTSTP's handler 
signal.signal(signal.SIGTSTP, myHandler)
signal.pause()
print('End of Signal Demo')


"""
在主程序中，我们首先使用signal.signal()函数来预设信号处理函数。
然后我们执行signal.pause()来让该进程暂停以等待信号，以等待信号。
当信号SIGUSR1被传递给该进程时，进程从暂停中恢复，并根据预设，
执行SIGTSTP的信号处理函数myHandler()。myHandler的两个参数一个用来识别信号(signum)，
另一个用来获得信号发生时，进程栈的状况(stack frame)。
这两个参数都是由signal.singnal()函数来传递的。
"""