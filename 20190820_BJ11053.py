#백준 11053번 가장 긴 증가하는 부분수열

n = int(input())
a = list(map(int, input().split(" ")[:n]))

d = [1]
for i in range(1, n):
    c = [1]
    for j in range(i):
        if a[j]<a[i]:
            c.append(d[j] + 1)
    d.append(max(c))

print(max(d))