
#백준 1890번

n = int(input())
a = list()
for _ in range(n):
    temp = list(map(int, input().split(" ")))
    a.append(temp)

b = [[0 for _ in range(n)] for _ in range(n)]
b[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break

        move = a[i][j]
        row = i + move
        col = j + move

        if row < n:
            b[row][j] += b[i][j]
        if col < n:
            b[i][col] += b[i][j]

print(b[-1][-1])