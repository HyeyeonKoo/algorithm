
#백준 13913 시간초과

def bfs(n, k):
    q = [[n, -1]]
    visit = list()
    while q:
        a = q.pop(0)
        loc = a[0]
        past = a[1]
        if loc == k:
            visit.append([loc, past])
            break
        else:
            if loc not in visit:
                visit.append([loc, past])
            for after in [loc-1, loc+1, loc*2]:
                if after not in visit and 0 <= after <= 100000:
                    q.append([after, loc])
    return visit


n, k = list(map(int, input().split()))
bfs(n, k)
visit = bfs(n, k)
answer = list()
past = -1
while visit:
    arr = visit.pop()
    if arr[0] == k:
        answer.append(arr[0])
        past = arr[1]
    else:
        if past == arr[0]:
            answer.append(arr[0])
            past = arr[1]
answer.reverse()
print(len(answer) - 1)
print(" ".join(map(str, answer)))