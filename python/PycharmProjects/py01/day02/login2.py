#!/root/nsd1905/bin/python
import getpass
username=input('Please enter your name: ')
password=getpass.getpass('Password: ')
if username=='bob' and password=='123456':
    print('Login Successful')
else:
    print('Login incorrect')