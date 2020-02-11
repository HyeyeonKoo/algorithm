
import heapq


def shortest_path(graph, start, finish):
    q = list()
    dist = {node:None for node in graph.keys()}
    before = {node:None for node in graph.keys()}

    heapq.heappush(q, [start, 0])
    dist[start] = 0

    while q:
        now_node, now_dist = heapq.heappop(q)
        for node in graph[now_node].keys():
            if dist[node] is None or now_dist + graph[now_node][node] < dist[node]:
                dist[node] = now_dist + graph[now_node][node]
                before[node] = now_node
                heapq.heappush(q, [node, dist[node]])

    print(start + " - " + finish)
    print("최단거리 : " + str(dist[finish]))
    print("최단경로 : " + finish + " -> ", end="")
    path = before[finish]
    while path:
        next = before[path]
        if next is None:
            print(path)
        else:
            print(path + " -> ", end="")
        path = next


mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
shortest_path(mygraph, "A", "F")
