n = int(input())

d = list()
d.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
d.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])

for i in range(2, n + 1):
    tmp = list()
    for j in range(0, 10):
        c = 0
        if j-1 > 0:
            c += d[i-1][j-1]
        if j+1 < 10:
            c += d[i-1][j+1]
        tmp.append(c%1000000000)
    d.append(tmp)

c = 0
for i in range(0, 10):
    c += d[-1][i]

print(c)