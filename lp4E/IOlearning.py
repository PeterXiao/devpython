__author__ = 'Administrator'
import os
path = os.environ["PATH"]
print(path)
import pickle
obj = SomeObject()
f = open("text.txt","wb")
pickle.dump(odj,f) #对象保存到f上
f.close()
#还原对象
'''
import pickle
f = open (filename,'rb')
obj = pickle.load(f)
f.close()
'''