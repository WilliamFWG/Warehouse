#!/root/mypy/bin/python

'''test try '''

try:
    n = input('Please enter a number: ')
    100/int(n)
except (ValueError,TypeError):
    print('Enter should be a number')
except  (KeyboardInterrupt,EOFError):
    print('User cancelled')
except ZeroDivisionError:
    print('%s cannot be a Zero ' % n)
else:
    print('100/%s= %5.2f' %(n,100/int(n)))
finally:
    print('Done')
