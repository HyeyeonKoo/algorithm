n = int(input())

d = [[0, 1]]

for i in range(1, n):
    d.append([d[i-1][0] + d[i-1][1], d[i-1][0]])

print(sum(d[n-1]))