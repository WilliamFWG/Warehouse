from urllib import request
import os
import sys


def graburl(url,dest,encoding=None):
    html=request.urlopen(url)
    if os.path.isfile(dest):
        os.mknod(dest)
    with open(dest, 'ab', encoding=encoding) as fobj:
        while 1:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    url=sys.argv[1]
    dest=sys.argv[2]
    #encoding='gbk'
    try:
        graburl(url,dest)
    except:
       print('Processing Failed')
    else:
       print('Processing Done')