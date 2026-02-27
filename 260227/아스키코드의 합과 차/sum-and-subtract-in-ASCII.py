a,b=input().split()
A=ord(a)
B=ord(b)
print(A+B,A-B if A>=B else B-A)
