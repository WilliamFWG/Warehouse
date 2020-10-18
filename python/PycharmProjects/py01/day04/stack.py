#!/root/nsd1905/bin/python
''' stack

append stack
pop stack
show stack
'''
stack=[]

def show_menu():
    menu='''
0) Push into Stack
1) Pull from Stack
2) Show Stack
3) Quit
Please Choose (0/1/2/3):'''
    cmds={'0':push_stack,'1':pull_stack,'2':show_stack}
    choice=''
    while choice!='3':
        choice=input(menu).strip()
        if choice not in ['0','1','2','3']:
            print('%s Invalid Entering' % choice)
            continue
        elif choice=='3':
            print('\nbye')
        else:
            cmds[choice]()

def push_stack():
    data=input("data: ").strip()
    if data:
        stack.append(data)
        print('OK! Pushing %s' % data)

def pull_stack():
    if stack:
        data=stack.pop()
        print('OK! Pull out %s' % data )
    else:
        print('Sorry!Nothing')

def show_stack():
    print(stack)

if __name__=='__main__':
    show_menu()
