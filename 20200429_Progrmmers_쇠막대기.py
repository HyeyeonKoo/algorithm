
# 프로그래머스 > 코딩테스트 연습 > 스택/큐 > 쇠막대기

from collections import deque

def solution(arrangement):
    answer = 0

    left = deque([])
    right = deque(arrangement)
    check = False
    while right:
        item = right.popleft()
        if item == "(":
            left.append(item)
            check = False
        else:
            if not check:
                left.pop()
                answer += len(left)
                check = True
            else:
                left.pop()
                answer += 1

    return answer