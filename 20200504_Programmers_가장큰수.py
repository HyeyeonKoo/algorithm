
# 프로그래머스 > 코딩테스트 연습 > 정렬 > 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*(12//len(x)), reverse=True)

    answer = ""
    if numbers[0] == "0":
        answer = "0"
    else:
        answer = ''.join(numbers)
        
    return answer