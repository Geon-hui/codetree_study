A=input().strip()
B=input().strip()

L=len(A)
found=False

for i in range(1,L+1):
    A=A[-1]+A[:-1]

    if A==B:
        print(i)
        found=True
        break
    
if not found:
    print(-1)