
#2019 카카오 신입개발자 코딩테스트
#괄호문자열 - 재귀문제

def right(q):

    if q[0] == ")" or q[-1] == "(":
        return False

    c = 0
    for i in range(len(q)):
        if q[i] == "(":
            c += 1
        elif q[i] == ")":
            c -= 1

    if c == 0:
        return True
    return False


def sepuv(p):

    u, v = "", ""
    c1, c2 = 0, 0
    for i in range(len(p)):
        if i == 0:
            if p[i] == "(": c1 += 1
            elif p[i] == ")": c2 += 1
        else:
            if p[i] == "(": c1 += 1
            elif p[i] == ")": c2 += 1
            if c1 == c2:
                u = p[:i+1]
                v = p[i+1:]
                return u, v


def solution(p):
    if p == "":
        return ""

    u, v = sepuv(p)
    if right(u):
        return u + solution(v)
    else:
        temp = "("
        ud = u[1:-1]
        for d in ud:
            if d == "(":
                temp += ")"
            if d == ")":
                temp += "("
        temp += ")" + solution(v)
        return temp


p = "(()())()"
print(solution(p))