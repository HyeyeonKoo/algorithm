
# 프로그래머스 > 코딩테스트 연습 > 스택/큐 > 기능개발

from collections import deque

def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        count = 0
        while progresses and progresses[0] > 100:
            progresses.popleft()
            speeds.popleft()
            count += 1

        if count != 0:
            answer.append(count)

    return answer