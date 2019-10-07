
#백준 2529
#파이썬으로 시간초과 문제가 해결되지 않음

import itertools

n = int(input())
alphabet = set()
words = list()
for _ in range(n):
    i = input()
    words.append(i)
    for a in i:
        alphabet.add(a)
alphabet = list(alphabet)
number = list()
num = 9
for _ in range(len(alphabet)):
    number.append(num)
    num -= 1

big = 0
if set(words) - set(alphabet) == set():
    for i in number:
        big += i
else:
    permutation = itertools.permutations(number)
    for per in permutation:
        hap = 0
        for word in words:
            sub = 0
            cnt = 0
            for w in word:
                sub += int(per[alphabet.index(w)])
                if cnt < len(word) - 1:
                    sub *= 10
                cnt += 1
            hap += sub

        if hap > big:
            big = hap
print(big)

