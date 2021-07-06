n = int(input())

dist = input().split()

x, y = 1, 1
# 각각 경우에 대해 처리
# 벗어나게 되면 무시함
for d in dist:
    if d == 'U':
        if y == 1:
            continue
        else:
            y -= 1
    elif d == 'D':
        if y == n:
            continue
        else:
            y += 1
    elif d == 'L':
        if x == 0:
            continue
        else:
            x -= 1
    elif d == 'R':
        if x == n:
            continue
        else:
            x += 1

print(y, x)