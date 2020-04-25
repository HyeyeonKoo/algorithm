
#백준 9663 N-Queen

def check(queen):
    for i in range(queen):
        if row[i] == row[queen]:
            return False
        if queen - i == abs(row[queen] - row[i]):
            return False
    return True

def go(queen):
    global result
    if queen == n:
        result += 1
    else:
        for i in range(n):
            row[queen] = i
            if check(queen):
                go(queen + 1)

n = int(input())
result = 0
row = [0] * n
go(0)
print(result)