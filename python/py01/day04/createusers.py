#!/root/nsd1905/bin/python
'''create a linux user

enter username (sys.argv[1])
generate 8 digits password
create user with the password generated
import the user and password into a specific file (sys.argv[2])
'''

import sys
import subprocess
import random

def gen_pass(n=8):
    str_pass=''
    for i in range(n):
        str_al=chr(random.randint(65,122))
        num=str(random.randint(0,9))
        str_pass+=random.choice([str_al,num])
    return str_pass


def create_user(username,passwd):
    idcheck='id '+username
    useradd='useradd ' + username
    passwdadd='echo ' + passwd +' | passwd --stdin '+username
    if subprocess.run(idcheck, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 1:
        subprocess.run(useradd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(passwdadd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result='0'
    else:
        result='1'
    return result


def writeintofile(content,filepath):
    with open(filepath,'a') as fobj:
        fobj.writelines(content)
    return '0'

if __name__=='__main__':
    if len(sys.argv[1])!=0 and len(sys.argv[2])!=0:
        passwd=gen_pass(8)
        print(passwd)
        print(sys.argv[1],sys.argv[2])
        result=create_user(sys.argv[1],passwd)
        if result=='0':
            content=[sys.argv[1],'  %s\n' % passwd]
            print(content)
            writeintofile(content,sys.argv[2])
        else:
            print('%s exists already.' % sys.argv[1])
    else:
        print('Parameters missing')



