__author__ = 'Administrator'
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