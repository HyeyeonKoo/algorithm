#백준 알고리즘 2156번 포도주 시식 문제
 
n = int(input())

d = list()

for i in range(n):
    a = int(input())
    if i == 0:
        d.append([0, a, 0])
    else:
        d.append([max(d[i-1]), a+d[i-1][0], a+d[i-1][1]])

print(max(d[n-1]))