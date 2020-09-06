import re

class AnalysisWebLog:
    def __init__(self,**args):
        if args.get('patt')=='ip':
            ip = '(\d{1,3}\.){3}\d{1,3}'
            self.mypattern = re.compile(ip)
        elif args.get('patt')=='br':
            br = 'Firefox|MSIE|Chrome|Safari'
            self.mypattern = re.compile(br)


    def countmypattern(self,fname):
        patt_dict={}
        with open(fname,'r') as fobj:
            while 1:
                line=fobj.readline()
                if not line:
                    break
                m=self.mypattern.search(line)
                if m:
                    key=m.group()
                    patt_dict[key]=patt_dict.get(key,0)+1
        return patt_dict


if __name__ == '__main__':
    fname='access_log-20200225'
    result1=AnalysisWebLog(patt='ip')
    print(result1.countmypattern(fname))
    result2=AnalysisWebLog(patt='br')
    print(result2.countmypattern(fname))
    result3=list(result2.countmypattern(fname).items())
    # print(result3)
    result3.sort(key=lambda seq:seq[1],reverse=True)
    print(result3)
