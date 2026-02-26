arr = input().strip()
L = len(arr)

# L회 반복
print(arr)
for _ in range(L):
    # 오른쪽으로 한 칸 밀기: 마지막 글자 + 처음부터 마지막 직전까지
    arr = arr[-1] + arr[:-1]
    print(arr)