A=input()
B=input()
count=0
while A!=B:
    A=A[-1]+A[:-1]
    count+=1
if count==0:
    print(-1)
else:
    print(count)