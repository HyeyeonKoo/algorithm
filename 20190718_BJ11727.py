n = int(input())
d = list()

d.append(1)
d.append(1)

for i in range(2, n+1):
    d.append(2 * d[i-2] + d[i-1])

print(d[n] % 10007)