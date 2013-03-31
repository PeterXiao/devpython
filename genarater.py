__author__ = 'Administrator'
import sys,os,glob
def quarters(next_quarter =0.0):
    while True:
        received =(yield next_quarter)
        if received is None:
            next_quarter += 0.25
        else:
            next_quarter =received
result =[]
generator = quarters()
while len(result)<5:
    x = next(generator)
    if abs(x -0.5)<sys.float_info.epsilon:
        x = generator.send(1.0)
    result.append(x)
#    print(x)


if sys.platform.startswith("win"):
    def get_file(names):
        for name in names:
            if os.path.isfile(name):
                yield name
            else:
                for file in glob.iglob(name):
                    if not os.path.isfile():
                        continue
                    yield  file
                    # print(file)
else :
    def get_file(names):
        return (file for file in names if os.path.isfile(file))