n,A=input().split()
n_int=int(n)
count=0
arr=[]
for i in range(n_int-1):
    val=input().strip()
    arr.append(val)
    if val==A:
        count+=1
print(count)
