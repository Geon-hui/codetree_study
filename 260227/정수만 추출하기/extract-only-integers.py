a,b=input().split()
result=''
result1=''

for ele in a:
    if ele.isdigit():
        result+=ele
    else:
        break
    a_int=int(result)
for ele1 in b:
    if ele1.isdigit():
        result1+=ele1
    else:
        break
    b_int=int(result1)
    
print(a_int+b_int)