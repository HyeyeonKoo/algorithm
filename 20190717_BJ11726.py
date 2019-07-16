n = input()
d = list()

d.append(1)
d.append(1)

for i in range(2, int(n)+1):
    d.append(d[i-1] + d[i-2])
    d[i] %= 10007

print(d[int(n)])