n, m = map(int, input().split())
cards = []

# 수를 리스트에 저장
for i in range(n):
    temp = list(map(int, input().split()))
    cards.append(temp)

# 가장 작은 수를 저장하는 리스트
mins = []
for i in range(n):
    mins.append(min(cards[i]))
# 이 리스트에서 가장 큰 수 <- 문제에서 원하는 정답
print(max(mins))