
# 프로그래머스 > 코딩테스트 연습 > 해시 > 베스트앨범

def solution(genres, plays):
    n = len(genres)

    genres_count = {}
    genres_num = {}
    for i in range(n):
        if genres[i] in genres_count.keys():
            genres_count[genres[i]] += plays[i]
        else:
            genres_count[genres[i]] = plays[i]
            genres_num[genres[i]] = 0

    songs = []
    for i in range(n):
        songs.append((genres[i], genres_count[genres[i]], plays[i], i))
    songs = sorted(songs, key=lambda x: (-x[1], -x[2], x[3]))

    answer = []
    for song in songs:
        if genres_num[song[0]] < 2:
            answer.append(song[3])
            genres_num[song[0]] += 1

    return answer