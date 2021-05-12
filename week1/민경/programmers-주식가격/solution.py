# 내 뒷 부분만 보고 비교하면 된다.
# 떨어지지 않은 기간 계산 > 떨어진 값까지 버텼다고 계산하기 때문에 값이 떨어진 경우 1을 더해줘야 한다.

def solution(prices):
    answer = []
    l = len(prices)
    for i in range(l):
        cnt = 0
        for j in range(i+1, l):
            if prices[i] > prices[j]:
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt)
    return answer