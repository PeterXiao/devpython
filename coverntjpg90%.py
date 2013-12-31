__author__ = 'Administrator'
import os
#os.popen(cmd)   要得到命令的输出内容，只需再调用下read()或readlines()等 如a=os.popen(cmd).read()
cmd ='convert -quality 90% '

#shell =cmd+''+''
#ends = os.popen(shell).read()
tmps =[]

filepth =[]
with open('list') as file:
    for line in file:
        #print(line)
        tmps.append(line.strip())
        filepth.append(line.strip()+'back')

#print(tmps)
#print(filepth)

for i in range(len(tmps)):
    log  = os.popen("echo " +tmps[i] +' '+filepth[i]).readline()
    log2 = os.popen("echo " +tmps[i] +' '+filepth[i]).readline() #将原始的img备份
    log3 = os.popen("echo " +tmps[i] +' '+filepth[i]).readline() #将装换结果改名成现在
    print(log,log2,log3)