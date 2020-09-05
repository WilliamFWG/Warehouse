import sys
def copy(src_name,dst_name):
    dst_obj=open(dst_name,'ab')
    with open(src_name,'rb') as src_obj:
        while 1:
            data=src_obj.read(4096)
            if not data:
                break
            dst_obj.write(data)
    dst_obj.close()
    cp_result='Success'
    return cp_result
a=copy(sys.argv[1],sys.argv[2])
print(a)