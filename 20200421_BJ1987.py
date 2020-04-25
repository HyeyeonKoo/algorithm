
#백준 1987 알파벳

def get_index(alphabet):
    return ord(alphabet) - 65

def dfs(x, y):
    global count, max_count
    visit[get_index(board[x][y])] = True
    for newX, newY in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
        if 0 <= newX < r and 0 <= newY < c:
            if not visit[get_index(board[newX][newY])]:
                if count+1 > max_count:
                    max_count = count+1
                count += 1
                dfs(newX, newY)
    visit[get_index(board[x][y])] = False
    count -= 1

r, c = map(int, input().split())
board = list()
for _ in range(r):
    temp = [i for i in input()]
    board.append(temp)
visit = [False]*26
count = 1
max_count = 1
dfs(0, 0)
print(max_count)