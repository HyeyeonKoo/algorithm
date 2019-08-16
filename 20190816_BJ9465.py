test_n = int(input())

for n in range(test_n):

    col_n = int(input())
    row1 = list(map(int, input().split(" ")[:col_n]))
    row2 = list(map(int, input().split(" ")[:col_n]))
    score = [row1, row2]

    d = [[0, score[0][0], score[1][0]]]
    for i in range(1, col_n):
        d.append([max(d[i-1]), score[0][i] + max(d[i-1][0], d[i-1][2]), score[1][i] + max(d[i-1][0], d[i-1][1])])

    print(max(d[-1]))