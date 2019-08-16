t = int(input())
d = list()

d.append(1)
d.append(2)
d.append(4)

for i in range(3, 11):
    d.append(d[i-3] + d[i-2] + d[i-1])

for i in range(t):
    n = int(input())
    print(d[n-1])