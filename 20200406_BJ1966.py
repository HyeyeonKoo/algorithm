#백준 1966번 프린터 큐
#난이도 : 하
#유형 : 큐, 구현, 그리디

test_num = int(input())

for _ in range(test_num):
    n, m = map(int, input().split(" "))
    value = [int(i) for i in input().split(" ")]
    value = [(v, i) for i, v in enumerate(value)]

    turn = 0
    while value:
        if value[0][0] == max([i[0] for i in value]):
            turn += 1
            if value[0][1] == m:
                print(turn)
                break
            else:
                value.pop(0)
        else:
            value.append(value.pop(0))
