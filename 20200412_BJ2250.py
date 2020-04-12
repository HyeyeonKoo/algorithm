#백준 2250 트리의 높이와 너비

class Node:
    def __init__(self, node, left, right):
        self.node, self.left, self.right = node, left, right

def in_order(node):
    if tree[node].left != -1:
        in_order(tree[node].left)
    tree_list.append(tree[node].node)
    if tree[node].right != -1:
        in_order(tree[node].right)

n = int(input())
tree, level = {}, {}
level_key, iter_base, iter_num, minus_cnt = 1, 1, 1, 0
for i in range(n):
    node, left, right = map(int, input().split())
    tree[node] = Node(node, left, right)
    if left == -1: minus_cnt -= 1
    if right == -1: minus_cnt -= 1
    if i + 1 == iter_num:
        if level_key in level.keys():
            level[level_key].append(node)
        else:
            level[level_key] = [node]
        iter_base *= 2
        iter_num = iter_num + iter_base + minus_cnt
        minus_cnt = 0
        level_key += 1
    else:
        if level_key in level.keys():
            level[level_key].append(node)
        else:
            level[level_key] = [node]

tree_list = list()
in_order(1)

result = []
for key in level.keys():
    dist = tree_list.index(max(level[key])) - tree_list.index(min(level[key])) + 1
    result.append((key, dist))

result = sorted(result, key=lambda x: (-x[1], x[0]))
print(result[0][0], result[0][1])

#아이디어는 맞았음
#그런데, 트리의 시작 지점이 항상 1이라는 보장이 없으므로, 그 때 런타임 에러가 발생함
#부모 노드를 고려해야 함!