#백준 1248번
#메모리 초과

from itertools import permutations

n = int(input())
si = input()
index = 0
s = list()
for i in range(n):
    temp = list()
    for j in range(i):
        temp.append("*")
    for j in range(i, n):
        temp.append(si[index])
        index += 1
    s.append(temp)

p = list(permutations([x for x in range(-10, 11)], n))

for each in p:
    check = True
    for i in range(n):
        for j in range(n):
            if s[i][j] == "*":
                continue
            hap = 0
            if i == j:
                hap = each[i] * 2
            else:
                for k in range(i, j + 1):
                    hap = hap + each[k]
            if hap > 0 and s[i][j] == "+":
                check = True
            elif hap == 0 and s[i][j] == "0":
                check = True
            elif hap < 0 and s[i][j] == "-":
                check = True
            else:
                check = False
            if check is False:
                break
        if check is False:
            break
    if check is True:
        print(" ".join(map(str, each)))
        break