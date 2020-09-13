import os
import time

print('Starting...')
rtvalue=os.fork()
if rtvalue:
    print('parent')
    result=os.waitpid(-1,0)
    print(result)
    time.sleep(5)
    print('Parent Done')
else:
    print('Child')
    time.sleep(10)
    print('Child Done')
