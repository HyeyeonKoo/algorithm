
# 프로그래머스 > 코딩테스트 연습 > 정렬 > H-Index

def solution(citations):
    citations.sort(reverse=True)

    for i, n in enumerate(citations):
        if n <= i:
            return i

    return len(citations)