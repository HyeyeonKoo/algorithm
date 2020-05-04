#백준 1781 컵라면
import heapq

n = int(input())
cup = list()
for _ in range(n):
    deadline, num = map(int, input().split())
    cup.append((deadline, num))
cup.sort()

result = list()
before = 0
for deadline, num in cup:
    heapq.heappush(result, num)
    if before == deadline:
        heapq.heappop(result)
    before = deadline
print(sum(result))