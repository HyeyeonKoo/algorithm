def solution(n, lost, reserve):
    
    answer = n - len(lost)

    for l in lost:
        if l in reserve:
            answer += 1
            del reserve[reserve.index(l)]
        elif l-1 in reserve and l-1 not in lost:
            answer += 1
            del reserve[reserve.index(l-1)]
        elif l+1 in reserve and l+1 not in lost:
            answer += 1
            del reserve[reserve.index(l+1)]

    return answer