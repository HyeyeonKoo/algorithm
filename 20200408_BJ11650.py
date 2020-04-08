
#백준 11650 좌표 정렬하기
#난이도 : 하
#문제유형 : 정렬

n = int(input())
xy = [tuple(list(map(int, input().split(" ")))) for _ in range(n)]
sorted_xy = sorted(xy)
for e in sorted_xy:
    print(e[0], e[1])
