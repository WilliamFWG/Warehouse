import  os

print('Starting....')
for i in range(3):
    rtvalue=os.fork()  #生成子进程 [1,2] 和[2]
    if not rtvalue:  #rtvalue 等于0时为子进程, if not rtvalue 即 判定该进程为子
        print('Hello world',rtvalue)
        exit()    #遇exit彻底结束
print('Done')