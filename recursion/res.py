__author__ = 'Peter xiao'
import os;
def list_dir(path, res):
    '''''
        res = {'dir':'root', 'child_dirs' : [] , 'files' : []}
        print list_dir('//root', res)
    '''
    for i in os.listdir(path):
        temp_dir = os.path.join(path,i)
        if os.path.isdir(temp_dir):
            temp = {'dir':temp_dir, 'child_dirs' : [] , 'files' : []}
            res['child_dirs'].append(list_dir(temp_dir, temp))
        else:
            res['files'].append(i)
    return res

def get_config_dirs(dir):
    res = {'dir':'root', 'child_dirs' : [] , 'files' : []}
    return list_dir(dir,res)

tmp = 'D:\python'
get_config_dirs(tmp)
print(get_config_dirs(tmp))