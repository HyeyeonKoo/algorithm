
#백준 5719 거의 최단 경로
import heapq
import copy

def bfs():
    q = list()
    heapq.heappush(q, (0, s))
    while q:
        nd, node = heapq.heappop(q)
        if node == d:
            dist[node] = dist[before[node]] + nd
            all_dist.add(copy.deepcopy(dist)[d])
        if visit[node] is False:
            if node == d:
                if visit.count(True) == n-1:
                    visit[node] = True
            else:
                visit[node] = True
            dist[node] = dist[before[node]] + nd
            if node in graph.keys():
                for nextNode in graph[node]:
                    if not visit[nextNode[1]]:
                        before[nextNode[1]] = node
                        heapq.heappush(q, nextNode)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    s, d = map(int, input().split())

    graph = dict()
    for _ in range(m):
        u, v, p = map(int, input().split())
        if u in graph.keys():
            graph[u].append((p, v))
        else:
            graph[u] = [(p, v)]

    all_dist = set()
    dist = [0] * n
    before = [-1] * n
    visit = [False] * n
    bfs()

    if len(all_dist) > 1:
        shortest = min(all_dist)
        all_dist.remove(shortest)
        next_min = min(all_dist)
        if next_min == shortest:
            print(-1)
        else:
            print(next_min)
    else:
        print(-1)