def solution(s: str):
    temp = []
    l = s[1:-1].replace('{', 'k').replace('}', 'k').split('k')[1:-1]
    # print(l)
    for each in l:
        if each != ',':
            temp.append(set(map(int, each.split(','))))
    temp.sort(key=lambda x: len(x))
    # print(temp)
    answer = [list(temp[0])[0]] * len(temp)
    for i in range(len(temp)-1):
        new_set = temp[i+1]-temp[i]
        # print(f'{temp[i+1]}  - {temp[i]} = {new_set}')
        answer[i+1] = new_set.pop()
    return answer


# print(solution('{{1},{1,2},{1,2,3},{1,2,3,4},{1,2,3,4,5}}'))
