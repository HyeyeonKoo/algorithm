import copy

def find(start_check, node, dist):
    global weight
    if node == end or (start_check is False and node == start):
        if node == end:
            weight.append(copy.deepcopy(dist))
        return
    for el in graph[node]:
        dist.append(el[1])
        find(False, el[0], dist)
        dist.pop()

N, M = map(int, input().split())
graph = dict()
for _ in range(M):
    a, b, c = map(int, input().split())
    if a in graph.keys():
        graph[a].append((b, c))
    else:
        graph[a] = [(b, c)]
    if b in graph.keys():
        graph[b].append((a, c))
    else:
        graph[b] = [(a, c)]
start, end = map(int, input().split())

weight = list()
find(True, start, [])
result = [min(i) for i in weight]
print(max(result))

#아이디어는 비슷했지만, 이진탐색을 이용해야 효율적으로 풀 수 있음!
#결국 target이 중량이므로, 중량을 빠르게 찾는 방법으로 풀어야 함
#중량 선택 -> bfs로 갈 수 있는지 확인!