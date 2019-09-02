import heapq

def solution(scoville, K):
    
    h = []
    for s in scoville:
        heapq.heappush(h, s)
    answer = 0

    while h[0] < K:
        try:
            heapq.heappush(h, heapq.heappop(h) + heapq.heappop(h)*2)
            answer += 1
        except Exception:
            return -1

    return answer