def gen_passwd(x=8):
    import random
    alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num='0123456789'
    count_num=random.choice(range(1,x))
    count_alpha=int(x)-int(count_num)
    n=1
    m=1
    plist=[]
    pword=''
    while n<=int(count_alpha):
        pick_alpha=random.choice(alpha)
        plist.append(pick_alpha)
        n+=1
    while m<=int(count_num):
        pick_num=random.choice(num)
        plist.append(str(pick_num))
        m+=1
    random.shuffle(plist)
    pword=''.join(plist)
    return pword

import sys
if __name__=='__main__':
    pslength=input('Please enter password length: ')
    if len(pslength)!=0:
        password=gen_passwd(int(pslength))
    else:
        password=gen_passwd()
    print(password)
