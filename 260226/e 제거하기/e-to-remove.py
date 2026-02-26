arr=input().rstrip()

index=arr.find('e')
li_arr=list(arr)
li_arr.pop(index)

print(''.join(li_arr))