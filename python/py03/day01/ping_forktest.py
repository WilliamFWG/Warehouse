import os
import subprocess

def ping(ip):
    result=subprocess.run('ping -c 2 %s &> /dev/null' % ip,shell=True)
    return result.returncode

if __name__ == '__main__':
    ips=('192.168.1.%s' % i for i in range(1,101))
#####################################################################
    #我的代码
    s=set()
    for ip in ips:
        rtvalue=os.fork()
        if not rtvalue:
            if ip not in s:         #集合处理重复ip ping,如果ip已经存在，则退出子进程
                s.add(ip)
                result=ping(ip)
                if result == 0:
                    print('%s:up' % ip)
                else:
                    print('%s:down' % ip)
                exit()
            else:
                exit()
######################################################################