arr=input()
li_arr=list(arr)
target1=li_arr[0]
target2=li_arr[1]
for i in range(len(li_arr)):
    if li_arr[i]==target2:
        li_arr[i]=target1
print(''.join(li_arr))