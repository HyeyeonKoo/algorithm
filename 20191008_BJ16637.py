
#백준 16637번
#마지막 한 개 테스트케이스 왜 틀리는지 원인을 모르겠음 ㅜㅜ

from itertools import combinations

n = int(input())
a = input()
num = list()
cal = list()
for i in range(n):
    if i % 2 == 0:
        num.append(int(a[i]))
    else:
        cal.append(a[i])

index = [i for i in range(len(num))][:-1]
comb = list()
for i in range(1, len(num)//2 + 1):
    temp = list(combinations(index, i))
    if not i == 1:
        for co in temp:
            if co[1] - co[0] > 1:
                comb.append(co)
    else:
        comb.extend(temp)

result = list()
for c in comb:
    temp_num = [x for x in num]
    temp_cal = [x for x in cal]
    i_minus = 0
    for i in c:
        temp = -1
        if temp_cal[i - i_minus] == "+": temp = temp_num[i - i_minus] + temp_num[i - i_minus + 1]
        elif temp_cal[i - i_minus] == "-": temp = temp_num[i - i_minus] - temp_num[i - i_minus + 1]
        elif temp_cal[i - i_minus] == "*": temp = temp_num[i - i_minus] * temp_num[i - i_minus + 1]
        del temp_num[i - i_minus]
        del temp_num[i - i_minus]
        del temp_cal[i - i_minus]
        temp_num.insert(i - i_minus, temp)
        i_minus += 1
    r = temp_num[0]
    for i in range(1, len(temp_cal) + 1):
        if temp_cal[i-1] == "+": r = r + temp_num[i]
        elif temp_cal[i-1] == "-": r = r - temp_num[i]
        elif temp_cal[i-1] == "*": r = r * temp_num[i]
    result.append(r)
    print(r)
print(max(result))