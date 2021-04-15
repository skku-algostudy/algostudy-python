# 시간초과 풀이

def solution(phone_book: list):
    phone_book.sort(key=lambda x: len(x))
    n = len(phone_book)
    for i in range(n-1):  # 0~n-2
        pfx: str = phone_book[i]
        for j in range(i+1, n):  # i+1~n-1
            if phone_book[j].startswith(pfx):
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
