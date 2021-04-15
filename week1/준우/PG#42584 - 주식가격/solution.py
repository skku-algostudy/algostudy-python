def solution(prices):
    n = len(prices)
    answer = []
    for i in range(n):
        price = prices[i]
        for j in range(i+1, n):
            if price > prices[j]:  # j시점에서 가격이 떨어졌다면
                break
        answer.append(j-i)
    return answer


print(solution([1, 2, 3, 2, 3]))
