#백준 1461 도서관

n, m = map(int, input().split())
cor = list(map(int, input().split()))
plus, minus = list(), list()
for i in cor:
    if i > 0:
        plus.append(i)
    else:
        minus.append(-i)
plus = sorted(plus, reverse=True)
minus = sorted(minus, reverse=True)

foot = 0
largest = 0

for item in [plus, minus]:
    index = 0
    while index < len(item):
        foot += item[index] * 2
        if item[index] > largest:
            largest = item[index]
        index += m

print(foot - largest)