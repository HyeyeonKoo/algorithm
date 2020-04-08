
#백준 10814 나이순 정렬
#난이도 : 하
#문제유형 : 정렬

n = int(input())
p = list()
for i in range(n):
    a, b = input().split(" ")
    p.append((i, int(a), b))
sp = sorted(p, key=lambda x: (x[1], x[0]))
for i in sp:
    print(i[1], i[2])




