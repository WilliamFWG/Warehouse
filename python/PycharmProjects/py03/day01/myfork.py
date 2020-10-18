import os
print('Starting.....')
return_value=os.fork()
if return_value==0:
    print(return_value,'hello from child')
else:
    print(return_value,'Hello World from parent')

print('Hello from both')