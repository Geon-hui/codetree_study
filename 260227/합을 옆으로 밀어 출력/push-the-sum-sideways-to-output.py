N=int(input())

result=0

for _ in range(N):
    arr=int(input())
    result+=arr
str_result=str(result)
print(str_result[1:]+str_result[0])