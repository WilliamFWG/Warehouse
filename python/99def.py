#!/root/mypy/bin/python
def Mutiple_table(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('%sX%s=%s' % (i,j,i*j), end=' ')
        print()

a=int(input('Please enter a number: '))
Mutiple_table(a)
