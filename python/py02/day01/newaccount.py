#!/root/nsd1905/bin/python
'''script for account

假设在记账时，有一万元钱
无论是开销还是收入都要进行记账
记账内容包括时间、金额和说明等
记账数据要求永久存储
'''

import pickle
import time
import os

acpath='/root/account.txt'


def show_menu():
    prmpt1='Income Amount: '
    prmpt2='Cost Amount: '
    prmpt3='Comments: '
    try:
        user_income=float(input(prmpt1))
        user_cost=float(input(prmpt2))
        assert user_income>=0 and user_cost>=0,'negetive value not acceptable'
        assert user_income>0 or user_cost>0 , 'Must have one enter more than Zero'
    except (ValueError,TypeError) as e1:
        print('Error Message: %s' % e1)
        exit()
    except (KeyboardInterrupt,EOFError):
        print('Good-Bye')
        exit()
    except AssertionError as e2:
        print(e2)
        exit()
    else:
        cmt=input(prmpt3)
        record_list=[time.strftime('%Y-%m-%d %H:%M:%S'),user_income,user_cost,user_income-user_cost,cmt]
        return record_list


def loadfrpickle(actbook=''):
    if not os.path.isfile(actbook):
        accountbook=open(actbook,'wb')
        title_list = [['Date', 'Income', 'Cost', 'Total', 'Comments'],]
        pickle.dump(title_list,accountbook)
        accountbook.close()
    else:
        accountbook = open(actbook, 'rb')
        account_list=pickle.load(accountbook)
        accountbook.close()
        return account_list

def writetolist(record_list=[],account_list=[]):
    record_list[-2]=float(account_list[-1][-2])+float(record_list[-2])
    account_list.append(record_list)
    return account_list


def dumptopickle(account_list=[],bkpath=''):
    accountbook=open(bkpath,'wb')
    pickle.dump(account_list,accountbook)
    accountbook.close()


if __name__ == '__main__':
    rd_list=show_menu()
    account_list=loadfrpickle(acpath)
    if account_list:
        new_list=writetolist(rd_list,account_list)
    else:
        new_list=loadfrpickle(acpath)
        new_list.append(rd_list)
    dumptopickle(new_list,acpath)
    result=loadfrpickle(acpath)
    for item in result:
        print('%-20s%-8s%-8s%-10s%-20s'% tuple(item))