a,b=input().split()

result= int(a)+int(b)
count=0

for ele in str(result):
    if ele=='1':
        count+=1
print(count)