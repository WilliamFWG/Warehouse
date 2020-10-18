import os
import time

print('Starting')
rtvalue=os.fork()
if rtvalue:
    print('Parent')
    time.sleep(30)
    print('Parent Done')
else:
    print('Child')
    time.sleep(10)
    print('Child Done')