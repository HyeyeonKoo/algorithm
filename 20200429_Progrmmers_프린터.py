
# 프로그래머스 > 코딩테스트 연습 > 스택/큐 > 프린터

from collections import deque

def solution(priorities, location):
    answer = 0

    priorities = deque(priorities)
    while priorities:
        if priorities[0] == max(priorities):
            priorities.popleft()
            answer += 1
            if location == 0:
                break
        else:
            priorities.append(priorities.popleft())

        if location == 0:
            location = len(priorities) - 1
        else:
            location -= 1

    return answer