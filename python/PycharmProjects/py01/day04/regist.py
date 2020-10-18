#!/root/nsd1905/bin/python
'''register

register menu 1/2/3
userdb={'name':'password'}
'''

import getpass

userdb={}

def show_menu():
    prmpt='''\
(1) Register
(2) Log-in
(3) Quit
Please choose (1/2/3): \
'''
    cmds={'1':register,'2':login}
    while 1:
        choice=input(prmpt).strip()
        if choice not in ('1','2','3'):
            print('Invalid Enter,try again')
        elif choice=='3':
            print('Bye-bye')
            break
        else:
            cmds[choice]()

def register():
    username=input('Username:').strip()
    if not username:
        print('Username cannot be blank')
        return
    if username in userdb:
        print('User already exists')
        return
    else:
        pwd=getpass.getpass('Password: ').strip()
        if pwd:
            userdb.update({username:pwd})
            print('Registration Success')
        else:
            print('No Password Entered')

def login():
    username = input('Username:').strip()
    if not username:
        print('Username cannot be blank')
        return
    else:
        pwd = getpass.getpass('Password: ').strip()
        if userdb.get(username)==pwd:
            print('Log-in Successfully')
        else:
            print('Invalid Username or Password')


if __name__=='__main__':
    show_menu()

