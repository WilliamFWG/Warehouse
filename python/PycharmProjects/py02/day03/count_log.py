
import re

def count_pattern(fname,patt):
    patt_dict={}
    mypattern=re.compile(patt)
    with open(fname,'r') as fobj:
        while 1:
            line=fobj.readline()
            if not line:
                break
            m=mypattern.search(line)
            if m:
                key=m.group()
                patt_dict[key]=patt_dict.get(key,0)+1
    return patt_dict

if __name__ == '__main__':
    fname='access_log-20200225'
    ip='(\d{1,3}\.){3}\d{1,3}'
    br='Firefox|MSIE|Chrome|Safari'
    result1=count_pattern(fname,ip)
    result2=count_pattern(fname,br)
    print(result1),print(result2)
    result3=list(result2.items())
    # print(result3)
    result3.sort(key=lambda seq:seq[1],reverse=True)
    print(result3)
