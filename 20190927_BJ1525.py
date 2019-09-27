
# 백준 1525번

start = ""
for i in range(3):
    start = start + "".join(input().split())
start = start.replace("0", "9")

q = [start]
d = {start: 0}

while q:
    new = q.pop(0)
    i = new.index("9")

    move = list()
    p = i // 3
    if p == 0:
        move.append(i + 3)
    elif p == 1:
        move.extend([i - 3, i + 3])
    elif p == 2:
        move.append(i - 3)
    r = i % 3
    if r == 0:
        move.append(i + 1)
    elif r == 1:
        move.extend([i - 1, i + 1])
    elif r == 2:
        move.append(i - 1)

    for m in move:
        temp = list(new)
        temp[i], temp[m] = temp[m], temp[i]
        next = "".join(temp)
        if next not in d:
            q.append(next)
            d[next] = d[new] + 1

if "123456789" in d:
    print(d["123456789"])
else:
    print(-1)
