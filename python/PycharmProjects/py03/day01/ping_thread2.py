import subprocess
import time
import threading

msg=''
class Ping:
    def __init__(self,ip):
        self.myip=ip
        global msg

    def __call__(self):
        result=subprocess.run('ping -c2 %s &> /dev/null' % self.myip,shell=True)
        if result.returncode == 0:
            msg='%s:up' % self.myip
        else:
            msg='%s:down' % self.myip

if __name__ == '__main__':
    ips = ('192.168.1.%s' % i for i in range(1,255))
    start_time=time.time()
    for ip in ips:
        #target 是ping的一个实例
        pingip_thread=threading.Thread(target=Ping(ip))
        pingip_thread.start()
        print(msg)
    end_time = time.time()
    print(end_time-start_time)