def get_whole_play_n(l):
    play_n = 0
    for each in l:
        play_n += each[1]
    return play_n


def solution(genres, plays):
    music_dict = {}
    answer = []
    for i, gp in enumerate(zip(genres, plays)):
        g, p = gp
        if g not in music_dict:
            music_dict[g] = [(i, p)]
        else:
            music_dict[g].append((i, p))
    for is_ps in sorted(music_dict.values(), key=get_whole_play_n, reverse=True):
        count = 0
        for i_p in sorted(is_ps, key=lambda x: x[1], reverse=True):
            if count >= 2:
                break
            i, _ = i_p
            answer.append(i)
            count += 1

    return answer


print(solution(["classic", "pop", "classic",
                "classic", "pop"], [500, 600, 150, 800, 2500]))
