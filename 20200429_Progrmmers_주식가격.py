
# 프로그래머스 > 코딩테스트 연습 > 스택/큐 > 주식가격

from collections import deque

def solution(prices):
    answer = []

    prices = deque(prices)
    while prices:
        price = prices.popleft()
        period = 0

        for nextPrice in prices:
            if nextPrice >= price:
                period += 1
            else:
                period += 1
                break

        answer.append(period)

    return answer