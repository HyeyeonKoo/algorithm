
# 프로그래머스 > 코딩테스트 연습 > 완전탐색 > 소수찾기

from itertools import permutations
import math

def solution(numbers):
    answer = 0

    max_num = int(1e7)  # 구할 범위 숫자 설정
    prime = [False, False] + [True]*max_num
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if prime[i]:
            for j in range(i+i, max_num, i):
                prime[j] = False

    possible = set()
    for i in range(1, len(numbers) + 1):
        possible = possible | set(permutations(numbers, i))
    possible = set(int("".join(item)) for item in possible)

    for num in possible:
        if prime[num]:
            answer += 1

    return answer