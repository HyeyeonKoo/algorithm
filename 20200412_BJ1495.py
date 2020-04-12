
#백준 1495번 기타리스트

n, s, m = map(int, input().split())
v = [int(i) for i in input().split()]

check = [[False]*(m+1) for _ in range(n + 1)]
check[0][s] = True

for i in range(1, n+1):
    for j in range(m+1):
        if check[i-1][j] is True:
            temp = j - v[i-1]
            if 0 <= temp <= m:
                check[i][temp] = True
            temp = j + v[i - 1]
            if 0 <= temp <= m:
                check[i][temp] = True

result = -1
for i in range(m, -1, -1):
    if check[-1][i]:
        result = i
        break
print(result)