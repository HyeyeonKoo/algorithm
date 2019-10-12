
# 백준 2251번

a, b, c = list(map(int, input().split(" ")))
cap = {"a": a, "b": b, "c": c}

q = [{"a": 0, "b": 0, "c": c}]
visit = [{"a": 0, "b": 0, "c": c}]
answer = list()
if b >= c: answer.append(0)

d = [("a", "b", "c"), ("a", "c", "b"), ("b", "a", "c"), ("b", "c", "a"), ("c", "a", "b"), ("c", "b", "a")]
while q:
    m = q.pop(0)
    if m["a"] == 0:
        answer.append(m["c"])

    for e in d:
        x, y, z = m[e[0]], m[e[1]], m[e[2]]
        if x < cap[e[1]] - y:
            x, y = 0, x + y
        elif x > cap[e[1]] - y:
            x, y = x - (cap[e[1]] - y), cap[e[1]]
        temp = {e[0]: x, e[1]: y, e[2]: z}
        if temp not in visit:
            visit.append(temp)
            q.append(temp)

answer = list(set(answer))
answer.sort()
print(" ".join(list(map(str, answer))))