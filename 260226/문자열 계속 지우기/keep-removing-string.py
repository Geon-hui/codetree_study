A = input()
B = input()

# Please write your code here.
while A.find(B)!=-1:
    index=A.find(B)
    A=A[:index]+A[index+len(B):]

print(A)

