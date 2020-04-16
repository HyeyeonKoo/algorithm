#백준 1092 배
from collections import deque

n = int(input())
ship = map(int, input().split())
m = int(input())
box = map(int, input().split())

ship = sorted(ship, reverse=True)
box = sorted(box, reverse=True)
box = deque(box)

if box[0] > ship[0]:
    print(-1)
else:
    count = 0
    ship_index = 0
    while box:
        b = box.popleft()
        if b <= ship[ship_index]:
            ship_index += 1
            if ship_index == n:
                ship_index = 0
                count += 1
        else:
            box.appendleft(b)
    if ship_index != 0:
        count += 1
    print(count)