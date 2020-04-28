
# 프로그래머스 > 코딩테스트연습 > 해시 > 완주하지 못한 선수

def solution(participant, completion):
    part = {}
    for one in participant:
        if one in part.keys():
            part[one] += 1
        else:
            part[one] = 1
    for one in completion:
        part[one] -= 1
    answer = ""
    for key in part.keys():
        if part[key] != 0:
            answer = key
            break
    return answer