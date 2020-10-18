#!/root/nsd1905/bin/ptyhon
import random
#1.shitou 2.jiandao 3.bu
all_choice=['shitou','jiandao','bu']
win_list=[['shitou','jiandao'],['jiandao','bu'],['bu','shitou']]
prmpt=''' 
1.shitou
2.jiandao
3.bu
qingchuquan
plz choose 1/2/3: '''
ren_score=0
cpt_score=0
while ren_score<=2 and cpt_score<=2:
    index=int(input(prmpt))
    ren=all_choice[index-1]
    cpt=random.choice(all_choice)
    print ("you choose %s, computer choose %s" % (ren,cpt))
    if ren==cpt:
        print('\033[32;1mequal\033[0m')
    elif [ren,cpt] in win_list:
        print('\033[31;1myou win\033[0m')
        ren_score+=1
    else:
        print('\033[33;1myou lose\033[0m')
        cpt_score+=1
    print('you win: %s , Computer win: %s' % (ren_score,cpt_score))
