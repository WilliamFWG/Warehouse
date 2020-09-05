#!/root/nsd1905/bin/python
''' This is a file creation script

test file creation

'''
import os
import shutil
import subprocess



if __name__=='__main__':
    newlist=[]
    newcontent=''
    while 1:
        filename=input('Please enter a file name with fullpath: ')
        #filepath=subprocess.run('pwd',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.decode('utf-8')
        if os.path.exists(filename):
            print(filename,'already exists.Try again')
            continue
        elif len(filename)==0:
            break
        else:
            newfile=open(filename,'a')
            while newcontent!='end':
                newcontent=input('enter \'end\' to stop > ')
                newlist.append(newcontent)
                continue
            newlist=['%s\n' % item for item in newlist ]
            for item in newlist:
                newfile.writelines(item)
            newfile.close()
            print('OK')
            break

