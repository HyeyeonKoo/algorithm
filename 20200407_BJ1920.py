
#백준 1920 수찾기
#난이도 : 하
#유형 : 해시,배열,구현

n = int(input())
n_list = set(map(int, input().split(" ")))
m = int(input())
m_list = map(int, input().split(" "))
for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)