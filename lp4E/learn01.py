'''
比较：
 包括数字在内的所有对象都可以进行 == 或者不等运算
'''

#对序列切片，slicing 语法为S[i:j] 从i开始包括第i个项目但是不包括第j个项目
#索引值均可为负数，表示S的相同项目L+n，大于等于L表示S的结尾，小于或者等于-L#的负索引表示S的开始 eg S[::-1]包含S所有项目，但是顺寻相反
#列表的编译方法，除了pop都返回None
#列表推导相当于调用结果列表的append方法建立相同列表的for循环
some_sequance = [1,2,3,4,5,6]
result = [x+1 for x in some_sequence]
result = [ x+1 for x in some_sequence if x >23]
result = [x+y for x in alist for y in another]
