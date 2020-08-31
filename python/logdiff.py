#!/root/mypy/bin/python
'''find the difference of two files

test

'''

import sys

def diff(fpath1,fpath2):
    f1=open(fpath1,'r')
    f2=open(fpath2,'r')
    f1set=set(f1.readlines())
    f2set=set(f2.readlines())
    fdiff=set(f1set-f2set)
    return fdiff

if __name__ == '__main__':
    result=diff(sys.argv[1],sys.argv[2])
    print(result)