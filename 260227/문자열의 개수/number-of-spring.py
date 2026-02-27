results = [] # 입력받은 문자열들을 담을 바구니

while True:
    arr = input().strip()
    if arr == '0':
        break
    
    results.append(arr) # 입력받은 것을 리스트에 추가

print(len(results))

# 저장된 리스트를 돌면서 짝수 번째(0, 2, 4...) 문자열만 출력
for i, val in enumerate(results):
    if i % 2 == 0:
        print(val)

