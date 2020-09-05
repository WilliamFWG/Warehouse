def mk_fib(b):
    fib=[0,1]
    b=int(b)
    for i in range(1,b-1):
        fib.append(fib[-2]+fib[-1])
    return fib

def isnumber(str):
    try:
        float(str)
    except ValueError:
    	return False
    else:
        return True

a=input('Please enter a number: ')
if isnumber(a):
    alist=mk_fib(a)
    print(alist)
else:
    print(a,' is not a number')

