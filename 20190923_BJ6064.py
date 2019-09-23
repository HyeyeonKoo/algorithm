
# 백준 6064번

t = int(input())

for _ in range(t):

    m, n, x, y = list(map(int, input().split()))
    x, y = x-1, y-1
    year = x
    while 1:
        if year % n == y:
            print(year + 1)
            break
        year += m
        if year > m*n:
            print(-1)
            break