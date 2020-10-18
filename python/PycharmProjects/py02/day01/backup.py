#!/root/nsd1905/bin/python
'''script for directory and file backup

by means of md5
Mon full backup
Tue-Sun incremental backup
计划任务,非交互式程序
1.星期几
2.备份方案（增量备和完全备）
完全备：
1.打包压缩目录下所有文件
2.os walk遍历所有文件并得到文件完整路径
3.计算每个文件的md5值
4.写入字典 -key: 路径 value md5
5.将字典pickle.dump到md5file里面

增量备
#压缩包的绝对路径： security_incr_back_20200904.tar.gz
#tar包生成并使用gz压缩
#将md5.data的值读出该字典
#os walk检查src的md5放进另一本字典中

#检查src中的每个key,是否在md5文件中有，如果没有，则是新增的文件。
#1.记录新增的key value，添加到md5文件中
#2.key文件路径加入tar包，作备份

# 检查src中的每个key是否在md5文件中有,如有，则看返回的value是否和生成的md5相同，如果不同，则
#1. 更新相应key的value在md5文件中
#2. key文件路径加入tar包，作备份
#关闭tar包
#把md5字典写入文件
'''

import tarfile
import time
import os
import pickle
import hashlib



def full_backup(src,dst,md5file):
    #压缩包的绝对路径： security_full_back_20200904.tar.gz
    fname='%s_full_backup_%s.tar.gz' % (os.path.basename(src),time.strftime('%Y%m%d'))
    fullpath=os.path.join(dst,fname)
    #打包并gz压缩
    tar=tarfile.open(fullpath,'w:gz')
    tar.add(src)
    tar.close()

    #计算每个文件的md5值


    #os.walk 得到每个文件完整路径
    md5dict={}
    for path,folders,files in os.walk(src):
        for file in files:
            key=os.path.join(path,file)
            #字典key=路径 value=md5
            md5dict[key] = check_md5(key)


    #把md5字典写入文件
    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)



def incr_backup(src,dst,md5file):
    #压缩包的绝对路径： security_incr_back_20200904.tar.gz
    fname='%s_incr_backup_%s.tar.gz' % (os.path.basename(src),time.strftime('%Y%m%d'))
    fullpath=os.path.join(dst,fname)
    #tar包生成并使用gz压缩
    tar=tarfile.open(fullpath,'w:gz')


    #将md5.data的值读出字典
    md5dict={}
    md5file_dict={}
    with open(md5file,'rb') as fobj:
        md5file_dict=pickle.load(fobj)
    #os walk检查src的md5放进另一本字典中
    for path,folders,files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key]=check_md5(key)
            #检查src中的每个key,是否在md5文件中有，如果没有，则是新增的文件。
            #1.记录新增的key value，添加到md5文件中
            #2.key文件路径加入tar包，作备份
            if md5file_dict.get(key)==None:
                md5file_dict[key]=md5dict[key]
                tar.add(key)
            # 检查src中的每个key是否在md5文件中有,如有，则看返回的value是否和生成的md5相同，如果不同，则
            #1. 更新相应key的value在md5文件中
            #2. key文件路径加入tar包，作备份
            elif md5file_dict.get(key)!=md5dict[key]:
                md5file_dict[key]=md5dict[key]
                tar.add(key)
    tar.close()
    #把md5字典写入文件
    with open(md5file,'wb') as fobj:
        pickle.dump(md5file_dict,fobj)













def check_md5(fname):   #文件名路径 ==》md5值
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while 1:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()





if __name__ == '__main__':
    src = '/tmp/demo/security'   #需要备份的目录
    dst = '/tmp/demo/backup'     #备份的目标目录
    md5file = '/tmp/demo/backup/md5.data'    #md5记录文件
    weekd = time.localtime()
    #校验是不是星期一？
    if weekd.tm_wday == 0:
        full_backup(src,dst,md5file)
    else:
        incr_backup(src,dst,md5file)

