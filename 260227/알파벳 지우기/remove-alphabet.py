a=input()
b=input()

result,result1="",""

for ele in a:
    if ele.isdigit():
        result+=ele
for ele1 in b:
    if ele1.isdigit():
        result1+=ele1

print(int(result)+int(result1))