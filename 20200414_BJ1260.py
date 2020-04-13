#백준 1260번 BFS와 DFS
from collections import deque

def dfs(v):
    # s = [v]
    # visit = [False] * (n + 1)
    # while s:
    #     v = s.pop()
    #     if not visit[v]:
    #         print(v, end=" ")
    #         visit[v] = True
    #         for nextV in graph[v]:
    #             if not visit[nextV]:
    #                 s.append(nextV)
    print(v, end=" ")
    visit[v] = True
    if v in graph.keys():
        for nextV in graph[v]:
            if not visit[nextV]:
                dfs(nextV)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not visit[v]:
            print(v, end=" ")
            visit[v] = True
            if v in graph.keys():
                for nextV in graph[v]:
                    if not visit[nextV]:
                        q.append(nextV)

n, m, v = map(int, input().split())
graph = dict()
for _ in range(m):
    a, b = map(int, input().split())
    if a in graph.keys():
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph.keys():
        graph[b].append(a)
    else:
        graph[b] = [a]

for key in graph.keys():
    graph[key].sort()

visit = [False] * (n+1)
dfs(v)
print()
visit = [False] * (n + 1)
bfs(v)

#딕셔너리 구조로 그래프를 구현할 때에는 키값이 있는지 체크하는 것이 중요!