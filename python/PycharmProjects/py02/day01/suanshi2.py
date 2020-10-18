#!/root/nsd1905/bin/python
'+- test'

import random

def exam():
    cmds={'+':lambda x,y:x+y,'-':lambda x,y:x-y}
    nums=[random.randint(1,100) for i in range(2)]   #random generate two numbers
    result=0
    nums.sort(reverse=True)    # sort the list to descent
    sign=random.choice("+-")   #random choose + or -
    result=cmds[sign](*nums)   #result = def plus or def minus

    prmpt='%d %s %d = ' % (nums[0],sign,nums[1])
    n=1
    while n<=3:
        try:
            quiz=int(input(prmpt))
        except ValueError:
            n+=1
            continue
        except (KeyboardInterrupt,EOFError):
            exit()
        if quiz==result:
            print('Very Good!')
            return
        else:
            print('Too bad')
            n+=1
    else:
        print(prmpt+str(result))







def main():
    while 1:
        exam()
        try:
            answer=input('Continue(y/n)?').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            answer='n'
        if answer in ('y','Y'):
            continue
        elif answer in ('n','N'):
            print('Bye-bye')
            break




if __name__ == '__main__':
   main()

