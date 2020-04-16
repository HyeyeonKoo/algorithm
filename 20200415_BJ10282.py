#백준 10282 해킹

import sys
sys.setrecursionlimit(100000)

def dfs(node):
    visit[node] = True
    if node in graph.keys():
        for nextNode in graph[node]:
            if not visit[nextNode[0]]:
                if time[node] + nextNode[1] < time[nextNode[0]]:
                    time[nextNode[0]] = time[node] + nextNode[1]
                dfs(nextNode[0])

case = int(input())

for _ in range(case):

    n, d, c = map(int, input().split())
    graph = dict()
    for _ in range(d):
        a, b, s = map(int, input().split())
        if b in graph.keys():
            graph[b].append((a, s))
        else:
            graph[b] = [(a, s)]

    visit = [False] * (n+1)
    time = [1e9] * (n+1)
    time[c] = 0
    dfs(c)

    print(visit.count(True), end=" ")
    max_t = 0
    for t in time:
        if t != 1e9 and t > max_t:
            max_t = t
    print(max_t)

#시간초과
#문제를 푼 방식은 비슷!, heapq를 이용한 다익스트라 알고리즘으로 풀어야 함!