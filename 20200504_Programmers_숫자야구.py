
# 프로그래머스 > 코딩테스트 연습 > 완전탐색 > 숫자야구


def solution(baseball):
    possible = [False]*111 + [True] * (1000 - 111)

    for number, strike, ball in baseball:
        number = str(number)

        for i in range(111, len(possible)):
            i = str(i)

            if "0" in i:
                possible[int(i)] = False
                continue

            same_check = False
            for j in range(3):
                for k in range(j+1, 3):
                    if i[j] == i[k]:
                        same_check = True
            if same_check:
                possible[int(i)] = False
                continue

            if possible[int(i)]:
                strike_count = 0
                for j in range(3):
                    if number[j] == i[j]:
                        strike_count += 1

                ball_count = 0
                for j in range(3):
                    ball_check = False
                    for k in range(3):
                        if j == k:
                            continue
                        if number[j] == i[k]:
                            ball_check = True
                    if ball_check:
                        ball_count += 1

                if strike != strike_count or ball != ball_count:
                    possible[int(i)] = False

    return possible.count(True)