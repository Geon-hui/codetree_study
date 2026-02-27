A=input().rstrip()
command_list=input()

for command in command_list:
    if command=='L':
        A=A[1:]+A[0]
    elif command=='R':
        A=A[-1]+A[:-1]
    else:
        break
print(A)