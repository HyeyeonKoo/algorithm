
#백준 2110 공유기 설치
#문제난이도 : 중
#문제유형 : 탐색

N, c = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

left, right = home[0], home[-1]
gap = 0

while left <= right:
    pin = (left + right) // 2
    count = 1
    check = home[0]
    for i in range(1, len(home)):
        if home[i] >= check + pin:
            check = home[i]
            count += 1
    if count >= c:
        left = pin + 1
        gap = pin
    else:
        right -= 1

print(gap)
