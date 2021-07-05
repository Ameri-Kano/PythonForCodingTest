n, k = map(int, input().split())

count = 0  # 횟수
# 나누어 떨어지면 나누고, 아니면 1을 빼기
# 이를 n이 1이 될 때까지 반복
while n > 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
    print(n)

print(count)