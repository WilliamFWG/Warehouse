#!/root/nsd1905/bin/python
def isnumber(str):
    try:
        float(str)
    except ValueError:
    	return False
    else:
        return True
score=input('Enter your score: ')
if isnumber(score):
    score=int(score)
    if score >=60 and score<=70:
        print ('Pass only')
    elif score>70 and score <=80:
        print('Not bad')
    elif score>80 and score<=90:
        print('Well done')
    elif score>90 and score<=100:
        print('Excellent')
    else:
        print('Failed')
else:
    print('Please enter number')