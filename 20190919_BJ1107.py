
#백준 1107
#테스트케이스는 다 맞았는데 자꾸 틀렸다는데... 어디서 틀린건지... 알 수가 없음

def compare(n, disable):
    num = str(n)
    for i in num:
        if int(i) in disable:
            return 0
    return len(str(n))

n = int(input())
m = int(input())
if m > 0:
    disable = list(map(int, input().split(" ")))
else:
    disable = list()

start = abs(n - 100)
answer = 500000

if start == 0 or start < len(str(n)):
    print(start)
else:
    for i in range(1000001):
        c = compare(i, disable)
        if not c == 0:
            temp = c + abs(n-i)
            if temp < answer:
                answer = temp
    print(answer)