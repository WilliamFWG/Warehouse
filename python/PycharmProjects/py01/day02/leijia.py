counter=0
result=0
cstr=[]
while counter<101:
    counter+=1
    if counter % 2:
        continue
    cstr.append(counter)
    result+=counter
print(result)
print(cstr)