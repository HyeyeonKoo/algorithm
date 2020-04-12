
#백준 1766 문제집

import heapq

n, m = map(int, input().split())
pre, visit = [0] * (n+1), [0] * (n+1)
for _ in range(m):
    after, before = map(int, input().split())
    pre[before] = after

base, temp = [i for i in range(1, n+1)], list()
result = list()
while base:
    one = heapq.heappop(base)
    if pre[one] == 0:
        result.append(one)
    else:
        if visit[pre[one]] != 0:
            result.append(one)
        else:
            temp.append(one)
            while base:
                two = heapq.heappop(base)
                if two == pre[one]:
                    result.append(two)
                    visit[two] = 1
                else:
                    temp.append(two)
            base = temp
            temp = list()

print(" ".join([str(i) for i in result]))

#아이디어는 비슷한데, 시간초과로 통과하지 못함
#위상정렬을 이용하면 이 문제를 시간 내에 풀 수 있음
#그리고, 한 문제에 선행되어야 하는 문제가 여러 개일 수 있으므로 pre가 이중리스트가 되어야 함