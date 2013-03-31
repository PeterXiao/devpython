__author__ = 'Administrator'
#避免副作用

#程序错误的大部分——并且这些问题驱使程序员去debug——出现是因为在程序的运行中变量获取了非期望的值。函数式编程简单地通过从不给变量赋值而绕过了这个问题。

# 剔除流程控制语句
def iflambda():
 namenum = lambda x: (x==1 and pr("one")) or (x==2 and pr("two"))  or (pr("other"))
 pr = lambda s:s

#将函数作为具有首要地位的对象
# 在Python中，函数就是另外一种我们能够就像某种处理的值。
'''
，将它们作为参数传递给函数式编程固有的函数map()、reduce()和filter()。这三个函数接受的第一个参数都是一个函数对象。
map()针对指定给它的一个或多个列表中每一项对应的内容，执行一次作为参数传递给它的那个函数 ，最后返回一个结果列表。
reduce()针对每个后继项以及最后结果的累积结果，执行一次作为参数传递给它的那个函数；例如，reduce(lambda n,m:n*m, range(1,10))是求"10的阶乘"的意思（换言之，将每一项和前面所得的乘积进行相乘）
filter()使用那个作为参数传递给它的函数，对一个列表中的所有项进行”求值“，返回一个由所有能够通过那个函数测试的项组成的经过遴选后的列表。


'''

#Python中的函数式循环
def oldfor():
  for e in lst:  func(e)      # statement-based loop
  map(func,lst)           # map()-based loop

def newfor():
     # let's create an execution utility function
     do_it = lambda f: f()
     # let f1, f2, f3 (etc) be functions that perform actions
     map(do_it, [f1,f2,f3])   # map()-based action sequence

#python  中的函数式循环
# statement-based while loop
'''while <cond>:
<pre-suite>
if <break_condition>:
break
else:
<suite>

# FP-style recursive while loop
def while_block():
    <pre-suite>
    if <break_condition>:
    return 1
else:
<suite>
return 0

while_FP = lambda: (<cond> and while_block()) or while_FP()
while_FP() '''


"""
# imperative version of "echo()"
def echo_IMP():
    while 1:
        x = raw_input("IMP -- ")
        if x == 'quit':
            break
        else
            print x
echo_IMP()

# utility function for "identity with side-effect"
def monadic_print(x):
    print x
    return x

# FP version of "echo()"
echo_FP = lambda: monadic_print(raw_input("FP -- "))=='quit' or echo_FP()
echo_FP()
"""

def bigmuls(x,y)
  bigmuls = lambda xs,ys: filter(lambda (x,y):x*y > 25, combine(xs,ys))
  combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
  dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
#print bigmuls((1,2,3,4),(10,15,3,22))