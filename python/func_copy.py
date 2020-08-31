#!/root/mypy/bin/python
def copy(srcfile_name,dstfile_name):
    srcfile_obj=open(srcfile_name,"rb")
    dstfile_obj=open(dstfile_name,'wb')
    while 1:
        data=srcfile_obj.read(4096)
        if not data:
            break
        dstfile_obj.write(data)
    srcfile_obj.close()
    dstfile_obj.close()

import sys
copy(sys.argv[1],sys.argv[2])
