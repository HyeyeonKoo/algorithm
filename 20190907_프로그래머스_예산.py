def solution(budgets, M):

    answer = 0

    if sum(budgets) <= M:
        answer = max(budgets)
    else:
        left = 0
        right = max(budgets)
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for b in budgets:
                if b < mid:
                    total += b
                else:
                    total += mid
            if total <= M:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

    return answer