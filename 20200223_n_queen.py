
def check(row, col, candidate):
    for i in range(row):
        if candidate[i] == col or abs(candidate[i] - col) == row - i:
            return False
    return True


def n_queen_dfs(n, row, candidate, result):
    if row == n:
        result.append(candidate[:])
        return
    for i in range(n):
        if check(row, i, candidate):
            candidate.append(i)
            n_queen_dfs(n, row+1, candidate, result)
            candidate.pop()


def n_queen(n):
    result = list()
    n_queen_dfs(n, 0, [], result)
    return result


print(n_queen(5))