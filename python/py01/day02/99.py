x=int(input('please enter a number: '))
for i in range(1,x+1):
    for j in range (1,i+1):
        print ('%s*%s=%s' % (i,j,i*j),end=' ')
    print()
