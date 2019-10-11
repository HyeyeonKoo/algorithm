
# 카카오 신입개발자 코딩테스트 3번

def turn90(key):
    n = len(key[0])
    new = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[j][n - i - 1] = key[i][j]
    return new


def check(test):
    n = len(test[0])
    for i in range(n):
        for j in range(n):
            if test[i][j] == 0:
                return False
    return True


def solution(key, lock):
    answer = True
    n = len(key[0])
    if n % 2 == 0:
        board = [[0]*(2*n) for _ in range(2*n)]
        m = n + 1
        s, e = (2*n)//2 - 1, (2*n)//2+1
    else:
        board = [[0]*(2*n+1) for _ in range(2*n+1)]
        m = n + 2
        s, e = (2*n-1)//2, (2*n-1)//2+3
    row, col = 0, 0
    for i in range(s, e):
        for j in range(s, e):
            board[i][j] = lock[row][col]
            col += 1
        row += 1
        col = 0

    for _ in range(4):
        for i in range(m):
            for j in range(m):
                test = [[x for x in y] for y in board]
                for k in range(n):
                    for l in range(n):
                        if test[i+k][j+l] == 0 and key[k][l] == 1:
                            test[i+k][j+l] = 1
                if check([x[s:e] for x in test[s:e]]):
                    return True
        key = turn90(key)
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))