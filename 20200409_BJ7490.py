#백준 7490 0 만들기
#문제난이도 : 중
#문제유형 : 재귀

def getGo(n, s, result):
    go = result
    if len(s) == 1:
        go = int(str(result) + str(n + 1))
    if len(s) > 2:
        if s[-2] == "+":
            go = result - int(s[-1]) + int(str(s[-1]) + str(n+1))
        elif s[-2] == "-":
            go = result + int(s[-1]) - int(str(s[-1]) + str(n+1))
        elif s[-2] == " ":
            go = int(str(result) + str(n+1))
    return go

def make0(n, s, result):
    if n == N:
        if result == 0:
            print(s)
        return
    make0(n+1, s + " " + str(n+1), getGo(n, s, result))
    make0(n+1, s + "+" + str(n+1), result + (n+1))
    make0(n+1, s + "-" + str(n+1), result - (n+1))


case = int(input())
for _ in range(case):
    N = int(input())
    make0(1, "1", 1)
    print()