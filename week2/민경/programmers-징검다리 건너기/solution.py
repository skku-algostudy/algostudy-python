# 이진 탐색으로 풀면 될거 같은데
# 테스트 1에서 런타임 에러가 계속 난다는건 내가 예외 처리를 못한다는건데
# 경계값, 반복문 맨 앞뒤 꼭 고려해서 에러 잡기

def solution(stones, k):
    def possible(std):
        jump = 1
        for stone in stones:
            if stone < std:
                jump += 1
            else:
                jump = 1
            if jump > k:    # 이게 맨 앞으로 가면 맨 뒤에서 문제가 생기는 경우를 잡지 못하니까
                return False
        return True

    def binary_search(start, end):
        mid = (start + end) // 2
        pos_std = possible(mid)
        if pos_std and not possible(mid+1):
            return mid
        elif pos_std:
            return binary_search(mid+1, end)
        else:
            return binary_search(start, mid-1)
    if len(stones) == 1:
        return stones[0]
    return binary_search(0, max(stones))

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([3], 1))