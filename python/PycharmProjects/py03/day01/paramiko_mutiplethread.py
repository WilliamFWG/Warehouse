from getpass import getpass
import threading
import paramiko
import sys
import os
#位置参数和默认值参数不可混用，位置参数必须在前，要不就全都使用默认值参数

def runcmd(ip,user='root',passwd=None,port=22,command=None):
    #print('I\'m def')
    output={'out':'','err':''}
    ssh=paramiko.SSHClient()  #创建客户端实例
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #自动回答yes
    try:
        ssh.connect(ip,username=user,password=passwd,port=port)               #链接各个ip地址
    except (paramiko.ssh_exception.NoValidConnectionsError,paramiko.ssh_exception.AuthenticationException) as a:
        print('connection failed  %s ' % a)
        return
    else:
        stdin,stdout,stderr=ssh.exec_command(command)
        out=stdout.read()
        err=stderr.read()
        if out:
            output['out']=out
        if err:
            output['err']=err
        print(' [\033[32;1m%s\033[0m] OUT:\n%s' % (ip, output['out'].decode()),
              '[\033[31;1m%s\033[0m] ERR:\n%s\n' % (ip, output['err'].decode())
              )
    finally:
        print('ssh close')
        ssh.close()


if __name__ == '__main__':
    if len(sys.argv)!=3:
        print('Usage:python %s ipfile command' % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('File %s does not exist' % sys.argv[1])
        exit(2)

    ipfile=sys.argv[1]
    command=sys.argv[2]
    passwd=getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip=line.strip() #去除行尾回车\n
            # runcmd(ip,passwd=passwd,command=command) #单线程处理
            #多线程处理
            runthread=threading.Thread(
                target=runcmd,args=(ip,),
                kwargs={'passwd':passwd,'command':command}
            )
            runthread.start()
            #print('[%s] OUT:\n%s\n' % (ip,output['out'].decode()),'[%s] ERR:\n%s\n' % (ip,output['err'].decode()))
