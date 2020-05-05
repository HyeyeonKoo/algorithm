
# 프로그래머스 > 코딩테스트연습 > 완전탐색 > 카펫

import math

def solution(brown, red):

    possible = []
    for i in range(1, int(math.sqrt(red)) + 1):
        if red % i == 0:
            possible.append((red//i, i))

    for hor, ver in possible:
        if (hor + 2) * (ver + 2) == brown + red:
            return [hor + 2, ver + 2]