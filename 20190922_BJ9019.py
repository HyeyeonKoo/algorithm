
# 백준 9019번
# Tip : 2차원 배열보다 1차원 배열을 사용하자! 

def cal_d(num):
    num = num*2
    if num > 9999:
        num = num % 10000
    return num


def cal_s(num):
    if num == 0:
        return 9999
    return num - 1


def cal_l(num):
    num = str(num)[1:] + str(num)[0]
    if num[0] != "0":
        return int(num)
    i = 0
    for one in num:
        if one == 0:
            i += 1
        else:
            break
    num = num[i - 1:]
    return int(num)


def cal_r(num):
    num = str(num)[-1] + str(num)[:-1]
    if num[0] != "0":
        return int(num)
    i = 0
    for one in num:
        if one == 0:
            i += 1
        else:
            break
    num = num[i - 1:]
    return int(num)


t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))

    q = [[a, "F"]]  # 계산할 숫자, 연산 이름
    visit = [[-1, "N"]]*10000  # 어디에서 왔는지, 연산 이름
    visit[a] = q[0]
    while q:
        n = q.pop(0)
        d = cal_d(n[0])
        if visit[d][0] == -1:
            q.append([d, "D"])
            visit[d] = [n[0], "D"]
        s = cal_s(n[0])
        if visit[s][0] == -1:
            q.append([s, "S"])
            visit[s] = [n[0], "S"]
        l = cal_l(n[0])
        if visit[l][0] == -1:
            q.append([l, "L"])
            visit[l] = [n[0], "L"]
        r = cal_r(n[0])
        if visit[r][0] == -1:
            q.append([r, "R"])
            visit[r] = [n[0], "R"]
        if n[0] == b:
            break

    index = b
    result = ""
    while 1:
        if visit[index][1] == "F":
            break
        else:
            result = visit[index][1] + result
        index = visit[index][0]
    print(result)
