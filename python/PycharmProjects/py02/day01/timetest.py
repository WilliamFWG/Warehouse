
import time

t1=time.time()
sum1=0
# for i in range(1,20000001):
#     sum=sum+i
# else:
sum1=sum(range(1,20000001))
t2=time.time()
print(sum1,t2-t1)