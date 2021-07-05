n, m, k = map(int, input().split())
l = list(map(int, input().split()))

l.sort(reverse=True)

# 가장 큰 수를 k번, 그 다음으로 큰 수를 1번 더함
# 이를 반복하여 총 m번 더하면 가장 큰 수가 됨
a = l[0]
b = l[1]
count = 0
result = 0
while count < m:
    for i in range(k):
        result += a
        count += 1
        if count == m:
            break
    result += b
    count += 1

print(result)