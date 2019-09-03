#벡준 1260번 DFS와 BFS

def bfs(graph, v):
    visit = []
    q = [str(v)]

    while q:
        n = q.pop(0)
        if n not in visit:
            visit.append(n)
            q.extend(graph[n])

    return visit

def dfs(graph, v):
    visit = []
    s = [str(v)]

    while s:
        n = s.pop()
        if n not in visit:
            visit.append(n)
            s.extend(graph[n])

    return visit

a = list(map(int, input().split(" ")))
n, m, v = a[0], a[1], a[2]
graph = dict()
for i in range(m):
    b = input().split(" ")
    if b[0] in graph.keys():
        graph[b[0]].append(b[1])
    else:
        graph[b[0]] = [b[1]]
    if b[1] in graph.keys():
        graph[b[1]].append(b[0])
    else:
        graph[b[1]] = [b[0]]

print(" ".join(dfs(graph, v)))
print(" ".join(bfs(graph, v)))