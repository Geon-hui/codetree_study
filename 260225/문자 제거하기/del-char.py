import sys
input=sys.stdin.readline().rstrip()

arr=input()
li_arr=list(arr)
number=[int(input()) for _ in range(len(arr)-1)]

for i in number:
    if i>len(li_arr):
        li_arr.pop(-1)
        print(''.join(li_arr))
    else:
        li_arr.pop(i)
        print(''.join(li_arr))

