
# 프로그래머스 > 코딩테스트연습 > 완전탐색 > 카펫

def get_graph(words):
    n = len(words[0])

    graph = {}
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue

            count = 0
            for k in range(n):
                if words[i][k] == words[j][k]:
                    count += 1

            if count >= n-1:
                if words[i] in graph.keys():
                    graph[words[i]].append(words[j])
                else:
                    graph[words[i]] = [words[j]]
    return graph

def dfs(node, target):
    if node == target:
        return
    visit[node] = True
    for next_node in graph[node]:
        if not visit[next_node]:
            before[next_node] = node
            dfs(next_node, target)

def solution(begin, target, words):
    global graph, visit, before

    words.append(begin)
    graph = get_graph(words)

    visit = {}
    before = {}
    for word in words:
        visit[word] = False
        before[word] = ""

    dfs(begin, target)

    answer = 0
    if target in before.keys():
        key = target
        while key != begin:
            answer += 1
            key = before[key]

    return answer