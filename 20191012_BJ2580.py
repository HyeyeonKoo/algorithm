
# 백준 2580 스도쿠

def check(sdoku):
    for i in range(9):
        row, col = [0] * 9, [0] * 9
        for j in range(9):
            if row[sdoku[i][j] - 1] == 0:
                row[sdoku[i][j] - 1] = 1
            else:
                return False
            if col[sdoku[j][i] - 1] == 0:
                col[sdoku[j][i] - 1] = 1
            else:
                return False
    for k in [0, 3, 6]:
        square = [0]*9
        for i in range(3):
            for j in range(3):
                if square[sdoku[k+i][k+j] - 1] == 0:
                    square[sdoku[k + i][k + j] - 1] = 1
                else:
                    return False
    return True


def solve(index):
    print(sdoku)
    if index >= len(blank):
        return check(sdoku)
    for i in range(1, 10):
        sdoku[blank[index][0]][blank[index][1]] = i
        if solve(index + 1):
            return True
        # False일 때를 잘 추가하면 풀릴 것 같은데...여기서 완전 막혔음


sdoku = list()
blank = list()
for i in range(9):
    sdoku.append(list(map(int, input().split(" "))))
    for j in range(9):
        if sdoku[i][j] == 0:
            blank.append((i, j))
solve(0)
print(sdoku)