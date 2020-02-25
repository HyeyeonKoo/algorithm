
#백준 1874번 스택 수열
#난이도 : 하
#유형 : 스택, 그리디

n = int(input())
arr = [int(input()) for _ in range(n)]
asc = [i+1 for i in range(n)]

stack, result = [asc.pop(0)], ["+"]
pin = 0
while stack or asc:
    if stack and stack[-1] == arr[pin]:
        stack.pop()
        result.append("-")
        pin += 1
    else:
        if asc:
            stack.append(asc.pop(0))
            result.append("+")
        else:
            break

if pin < n-1:
    print("NO")
else:
    print("\n".join(result))