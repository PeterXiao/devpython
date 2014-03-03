__author__ = 'Administrator'
import multiprocessing
import string
import collections
import itertools
import multiprocessing


class SimpleMapReduce(object):



    def __init__(self, map_func, reduce_func, num_workers=None):
        """
        map_func是一个用实现映射（对一些独立元素组成的概念上的列表（例如，一个测试成绩的列表）的每一个元素进行指定的操作（
        有人发现所有学生的成绩都被高估了一分，他可以定义一个“减一”的映射函数，用来修正这个错误。）。事实上，每个元素都是被独立操作的，
        而原始列表没有被更改，因为这里创建了一个新的列表来保存新的答案）的函数



        reduce_func是一个用于化简（对一个列表的元素进行适当的合并（如果有人想知道班级的平均分该怎么做？他可以定义一个化简函数，
        通过让列表中的元素跟自己的相邻的元素相加的方式把列表减半，如此递归运算直到列表只剩下一个元素，然后用这个元素除以人数，
        就得到了平均分。）。虽然他不如映射函数那么并行，但是因为化简 总是有一个简单的答案，大规模的运算相对独立）的函数
        num_workers是进程池的数量这里默认就是cpu数目"""
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)



    def partition(self, mapped_values):  #组织k-v映射，返回一个键和一个值序列元组的无序序列
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()



    def __call__(self, inputs, chunksize=1):  #inputs是一个包含输入的数据进行处理的迭代器 chunksize用来调整映射效果
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        partitioned_data = self.partition(itertools.chain(*map_responses))
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values
def file_to_words(filename):
    STOP_WORDS = set([
            'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if', 'in',
            'is', 'it', 'of', 'or', 'py', 'rst', 'that', 'the', 'to', 'with',
            ])
    TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))



    print multiprocessing.current_process().name, 'reading', filename
    output = []



    with open(filename, 'rt') as f:
        for line in f:
            if line.lstrip().startswith('..'): # Skip rst comment lines
                continue
            line = line.translate(TR) # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append( (word, 1) )
    return output   #读取文件并返回一个值（词，字符串）序列



def count_words(item):
    word, occurances = item
    return (word, sum(occurances))  #转换成包含单词和其数量的元组



if __name__ == '__main__':
    import operator
    import glob



    input_files = glob.glob('*.rst')



    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()



    print '\nTOP 20 WORDS BY FREQUENCY\n'
    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    for word, count in top20:
        print '%-*s: %5s' % (longest+1, word, count)