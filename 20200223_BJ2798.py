#백준 2798번 블랙잭
#난이도 : 하
#유형 : 배열, 완전탐색
from itertools import combinations

n, m = map(int, input().split(" "))
n_list = list(map(int, input().split(" ")))
n_list.sort()

hap = sum(n_list[:3])
candidate = combinations(n_list, 3)

for item in candidate:
    if hap < sum(item) <= m:
        hap = sum(item)

print(hap)