#백준 1774 우주신과의 교감
import math
import itertools

n, m = map(int, input().split())
god = [(0, 0, 0)]
for i in range(n):
    x, y = map(int, input().split())
    god.append((i+1, x, y))
exist = list()
for _ in range(m):
    n1, n2 = map(int, input().split())
    exist.append((n1, n2))

dist = [[0]*(n+1)]
for i in range(1, n+1):
    temp_dist = [0]
    for j in range(1, n+1):
        temp_dist.append(math.sqrt((god[i][1] - god[j][1])**2 + (god[i][2] - god[j][2])**2))
    dist.append(temp_dist)

possible = list(itertools.permutations(god[1:], n))
shortest = 1e9
for p in possible:
    link_check = True
    for i in range(len(p)):
        for j in range(len(exist)):
            if p[i][0] == exist[j][0]:
                if i > 0 and p[i-1][0] == exist[j][1]:
                    link_check = True
                elif i < len(p) - 1 and p[i+1][0] == exist[j][1]:
                    link_check = True
                else:
                    link_check = False

    if link_check:
        total_dist = 0
        for i in range(1, len(p)):
            total_dist = total_dist + dist[p[i-1][0]][p[i][0]]
        if total_dist < shortest:
            shortest = total_dist

for e in exist:
    shortest -= dist[e[0]][e[1]]
print("%.2f" % shortest)

#메모리 초과
#그래프와 Union - Find 알고리즘을 이용해야 함