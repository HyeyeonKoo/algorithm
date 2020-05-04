
# 프로그래머스 > 코딩테스트 연습 > 힙(Heap) > 라면공장

import heapq

def solution(stock, dates, supplies, k):
    answer = 0

    start = 0
    max_supply = []

    while stock < k:
        for i in range(start, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(max_supply, -supplies[i])
            start += 1

        stock += (heapq.heappop(max_supply) * -1)
        answer += 1

    return answer