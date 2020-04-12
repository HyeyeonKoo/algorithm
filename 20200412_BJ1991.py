
#백준 1991 트리순회

class Node:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right

def pre_order(node):
    print(node.node, end="")
    if node.left != ".":
        pre_order(tree[node.left])
    if node.right != ".":
        pre_order(tree[node.right])

def in_order(node):
    if node.left != ".":
        in_order(tree[node.left])
    print(node.node, end="")
    if node.right != ".":
        in_order(tree[node.right])

def post_order(node):
    if node.left != ".":
        post_order(tree[node.left])
    if node.right != ".":
        post_order(tree[node.right])
    print(node.node, end="")

n = int(input())
tree = {}
for i in range(n):
    node, left, right = input().split()
    tree[node] = Node(node, left, right)

pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])
