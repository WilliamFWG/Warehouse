import subprocess
import time

def ping(ip):
    result=subprocess.run('ping -c2 %s &> /dev/null' % ip,shell=True)
    return result.returncode

if __name__ == '__main__':
    ips = ('192.168.1.%s' % i for i in range(1,255))
    start_time=time.time()
    for ip in ips:
        result=ping(ip)
        if result==0:
            print('%s:up' % ip)
            continue
        print('%s:down' % ip)
    end_time = time.time()
    print(end_time-start_time)