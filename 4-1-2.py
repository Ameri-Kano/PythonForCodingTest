n = int(input())

# 시간을 문자열로 바꾼 이후 3이 포함되어있는지 확인
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                count += 1

print(count)
