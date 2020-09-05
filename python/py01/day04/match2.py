match=0
while match<=3:
    for i in range(ord('a'),ord('c')+1):
        for j in range(ord('x'),ord('z')+1):
            if i==ord('a') and j==ord('x'):
                continue
            elif i==ord('c') and (j==ord('x') or j==ord('z')):
                continue
            else:

                match+=1
                print('%s vs %s' % (chr(i),chr(j)))


