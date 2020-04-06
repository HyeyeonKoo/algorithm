#백준 5397 키로거
#난이도 : 중
#유형 : 스택, 구현, 그리디

test_num = int(input())

for _ in range(test_num):
    log = input()
    left, right = list(), list()

    for ch in log:
        if ch == "<":
            if left:
                right.append(left.pop())
        elif ch == ">":
            if right:
                left.append(right.pop())
        elif ch == "-":
            if left:
                left.pop()
        else:
            left.append(ch)
    left.extend(reversed(right))
    print("".join(left))