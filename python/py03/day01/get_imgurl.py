import wget
import os
import sys
import re
from urllib import error

def get_patt(fname,patt,encoding=None):
    match_list=[]
    mypatt = re.compile(patt)
    with open(fname,encoding=encoding) as fobj:
        for line in fobj:
            matchdata=mypatt.search(line)
            if matchdata:
                match_list.append(matchdata.group())
    return match_list


if __name__ == '__main__':
    html=sys.argv[1]
    filedest=sys.argv[2]
    encoding=sys.argv[3]
    folddest=os.path.dirname(filedest)
    #如果不存在目录，则创建：
    if not os.path.isdir(folddest):
        try:
            os.makedirs(folddest)
        except:
            print('Invalid folder %s' % filedest)
            exit()
    #如果不存在文件则下载
    if not os.path.isfile(filedest):
        wget.download(html, filedest)
    #获取页中的所有图片链接
    img_pattern= '(http|https)://[/\w.-]+\.(jpg|png|jpeg|gif)'
    img_list=get_patt(filedest, img_pattern,encoding)
    #print(img_list)
    for url in img_list:
        try:
            wget.download(url,folddest)
        except (error.HTTPError,error.URLError):
            print('%s failed' % url)
            with open(os.path.join(folddest,'img_failed.txt'),'a+') as fobj:
                fobj.write('%s\n' % url)




