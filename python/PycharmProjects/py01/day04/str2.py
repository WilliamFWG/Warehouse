from random import randint

nums=[randint(1,100)for i in range(10)]
for i in range(len(nums)):
    print(i,nums[i])

for data in enumerate(nums):
    print(data)

for ind,num in enumerate(nums):
    print(ind,num)
