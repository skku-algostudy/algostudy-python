def solution(ops):
    l = []
    for op in ops:
        if op[0] == 'I':  # 삽입
            num = int(op[2:])
            l.append(num)
        elif l:
            if op[2] == '1':  # 최댓값 삭제
                del l[l.index(max(l))]
            else:
                del l[l.index(min(l))]

    if l:
        return [max(l), min(l)]
    return [0, 0]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
