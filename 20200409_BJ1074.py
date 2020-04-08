#백준 1074 Z
#문제난이도 : 중
#문제유형 : 재귀

def funcz(n, x, y):
    global count
    if n == 2:
        if x == r and y == c:
            print(count)
            return
        count += 1
        if x == r and y + 1 == c:
            print(count)
            return
        count += 1
        if x + 1 == r and y == c:
            print(count)
            return
        count += 1
        if x + 1 == r and y + 1 == c:
            print(count)
            return
        count += 1
        return
    funcz(n/2, x, y)
    funcz(n/2, x, y + n/2)
    funcz(n/2, x + n/2, y)
    funcz(n/2, x + n/2, y + n/2)


n, r, c = map(int, input().split(" "))
count = 0
funcz(2**n, 0, 0)