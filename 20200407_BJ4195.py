
#백준 4195 친구 네트워크
#난이도 : 중
#유형 : 해시,집합,그래프


def find(f):
    if f == parent[f]:
        return f
    else:
        p = find(parent[f])
        parent[f] = p
        return parent[f]


def union(f1, f2):
    f1 = find(f1)
    f2 = find(f2)

    if f1 != f2:
        parent[f2] = f1
        length[f1] += length[f2]


case = int(input())
for _ in range(case):
    F = int(input())

    parent = dict()
    length = dict()

    for _ in range(F):
        f1, f2 = input().split()

        if f1 not in parent:
            parent[f1] = f1
            length[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            length[f2] = 1

        union(f1, f2)
        print(length[find(f1)])