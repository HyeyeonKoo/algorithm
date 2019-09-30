
#백준 14501번

n = int(input())
t = list()
p = list()
for i in range(n):
    temp = input().split(" ")
    t.append(int(temp[0]))
    p.append(int(temp[1]))

d = [0]*n

if t[-1] == 1:
    d[-1] = p[-1]

for i in range(n-2, -1, -1):
    day = i + t[i]
    if day == n:
        d[i] = max(p[i], d[i+1])
    elif day < n:
        d[i] = max(p[i] + d[day], d[i+1])
    elif day > n:
        d[i] = d[i+1]

print(d[0])