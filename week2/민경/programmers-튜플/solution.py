def solution(s):
    s = s[2:-2].split('},{')
    temp = []
    for tup in s:
        temp.append(set(list(map(int, tup.split(',')))))
    temp = sorted(temp, key=lambda x: len(x))

    answer = [*temp[0]]
    for i in range(1, len(temp)):
        answer.append(*(temp[i] - temp[i - 1]))
    return answer
