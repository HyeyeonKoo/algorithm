
# 프로그래머스 > 코딩테스트 연습 > 해시 > 전화번호 목록

def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        l = len(phone_book[i])
        for j in range(len(phone_book)):
            if len(phone_book[j]) > l and phone_book[j][:l] == phone_book[i]:
                answer = False
                break
        if answer is False:
            break
    return answer