__author__ = 'Administrator'
pr = lambda s:s
namenum = lambda x: (x==1 and pr("one")) \
                  or (x==2 and pr("two")) \
                 or (pr("other"))

print( namenum(1) \
       ,namenum(2) \
       ,namenum(3))
	   
	   
	   
"""
map()针对指定给它的一个或多个列表中每一项对应的内容，
     执行一次作为参数传递给它的那个函数 ，最后返回一个结果列表。
reduce()针对每个后继项以及最后结果的累积结果，
       执行一次作为参数传递给它的那个函数；
	   例如，reduce(lambda n,m:n*m, range(1,10))是求"10的阶乘"的意思
	   （换言之，将每一项和前面所得的乘积进行相乘）
filter()使用那个作为参数传递给它的函数，
         对一个列表中的所有项进行”求值“，
		 返回一个由所有能够通过那个函数测试的项组成的经过遴选后的列表。
"""
'''
for e in lst:  func(e)      # statement-based loop
map(func,lst)           # map()-based loop

# let's create an execution utility function
do_it = lambda f: f()

# let f1, f2, f3 (etc) be functions that perform actions

map(do_it, [f1,f2,f3])   # map()-based action sequence
'''
"""
# statement-based while loop
while <cond>:
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
while_FP()
"""