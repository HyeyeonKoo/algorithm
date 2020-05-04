
# 프로그래머스 > 코딩테스트 연습 > 힙(Heap) > 이중우선순위큐

import heapq

def solution(operations):
    max_q = []
    min_q = []

    for op in operations:
        if op[0] == "I":
            num = int(op.split()[1])
            heapq.heappush(max_q, num * -1)
            heapq.heappush(min_q, num)
        elif op == "D 1":
            if max_q:
                num = heapq.heappop(max_q)
                del min_q[min_q.index(num*-1)]
        elif op == "D -1":
            if min_q:
                num = heapq.heappop(min_q)
                del max_q[max_q.index(num*-1)]

    answer = []
    if max_q:
        answer.append(heapq.heappop(max_q) * -1)
    else:
        answer.append(0)
    if min_q:
        answer.append(heapq.heappop(min_q))
    else:
        answer.append(0)

    return answer