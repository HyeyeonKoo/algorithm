
# 프로그래머스 > 코딩테스트 연습 > 스택/큐 > 탑

def solution(heights):
    n = len(heights)
    answer = [0]*n
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            if heights[j] > heights[i]:
                answer[i] = j + 1
                break
    return answer