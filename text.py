import os
import sys
def testFunc(arg1,*arg, **args):
    """
    This is a test docs
    """
    print(args)
    print(arg)
    print(arg1)
    

# testFunc(1,2,3,4,num=3,num1=4)
if __name__ == '__main__':
    testFunc(1,2,3,4,num=3,num1=4)