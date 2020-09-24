import paramiko
ssh=paramiko.SSHClient()   #创建实力
#相当于链接服务器时，自动回答yes
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('192.168.1.100',username='root',password='123456')
except paramiko.ssh_exception.NoValidConnectionsError as a:
    print('connection failed  %s ' %a )
else:
    #执行命令指令，返回元组，元组有三项 输入，输出，错误的类文件对象
    stdin,stdout,stderr=ssh.exec_command('ls -l /root/')
    #打印出内容到屏幕， decode()解码方式输出utf8
    print(stdout.read().decode())
finally:
    #关闭链接
    ssh.close()