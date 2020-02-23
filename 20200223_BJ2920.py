#백준 2920번 음계
#난이도 : 하
#유형 : 배열, 구현

i = list(map(int, input().split(" ")))
asc = sorted(i)
desc = sorted(i, reverse=True)
if i == asc:
    print("ascending")
elif i == desc:
    print("descending")
else:
    print("mixed")