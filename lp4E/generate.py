__author__ = 'Administrator'
def countdown(n):
    print("Counting Down!")
    while n >0:
        yield n # 生成一个值（n）
        n -= 1
c = countdown(5)
print(c.__next__())