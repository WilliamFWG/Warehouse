#!/root/nsd1905/bin/python
'''get the required data in a certain time range from a file

'''

import time

with open('/root/file.txt','r') as f:
    filelist=f.readlines()
    for item in filelist:
        txnlist=item.strip().split()
        txndate=txnlist[0]+' '+txnlist[1]
        txnvalue=txnlist[2]
        if time.strptime('2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S')<time.strptime(txndate,'%Y-%m-%d %H:%M:%S')<time.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S'):
            print(txndate,txnvalue)



