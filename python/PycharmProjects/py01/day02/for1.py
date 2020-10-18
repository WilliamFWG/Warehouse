a=0
b=1
result=[a,b]
x=int(input('please enter a number: '))
for i in range(3,x+1):
    temp=a+b
    result.append(temp)
    a=b
    b=temp
print(result)