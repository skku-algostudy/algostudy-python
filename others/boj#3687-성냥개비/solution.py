from itertools import combinations_with_replacement

t = int(input())
nums = []
for i in range(t):
    nums.append(int(input()))

for num in nums:
    mini, maxi = '', ''
    # 가장 작은 수
    # 그 숫자 자릿수 안에서 가능한 경우까지 연산한 후에 그 안에서 최소를 찾아야 한다.
    idx = [2, 3, 4, 5, 6, 7]    # 사용한 성냥개비 개수
    val = [1, 7, 4, 2, 0, 8]    # 그에 따른 숫자
    if num in idx:  # 한 자리수일 때.. 가 아니라 7 이하일 때, 아 그 전 값이 올 수..
        if num == 6:
            mini = 6
        else:
            mini = val[idx.index(num)]
    else:   # 8이 성냥개비 제일 많이 쓰는거니까

        moc = num//7
        if num%7 == 0:
            mini = '8' * moc

        else:
            candi = [n for n in combinations_with_replacement(idx, moc+1) if sum(n) == num]
            change = []
            for c in candi:
                number = []
                for i in c:
                    number.append(val[idx.index(i)])
                number.sort()
                if number[0] == 0:
                    j = 0
                    for j in range(len(number)):
                        if number[j] != 0:
                            break
                    if number[j] > 6 or number[-1] == 0:
                        number[0] = '6'
                    else:
                        number[0], number[j] = number[j], number[0]
                change.append(''.join(list(map(str, number))))
            mini = min(change)

    # 가장 큰 수
    if num%2 == 0:
        maxi = '1'*(num//2)
    else:
        maxi = '7'+'1'*(num//2-1)
    print(int(mini), int(maxi))
