__author__ = 'luozi'
import random
I2=[]
I1 =range(1,10001)
while len(I1)>0:
    x =random.randint(0,len(I1)-1)
    a =I1[x]
    I2.append(a)
    I1.pop(x)
print(I2)

def text():
    while 1:
        put = raw_input(' input something')
        try:
            put =int(put)
            if put%2 ==0:
                print()
                break
            else:
               print()
               break
        except:
            put =str(put)
            if not ' ' in put:
                print(len(put))
                break
            else:
                print(put.count(' '))
                break