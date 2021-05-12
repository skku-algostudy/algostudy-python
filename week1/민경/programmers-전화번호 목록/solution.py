# 그냥 정렬하면 될거 같아서 sort 하고 버블정렬처럼 두개씩 비교해주도록 구현
# startswith 함수 > string.startswith("시작 문자열") 으로 길이 체크 및 리스트 비교를 대치해줄 수 있습니다
# 역시 파이썬 최고
# + 처음에 아무 생각 없이 in 함수 썼다가 하나만 안 통과돼서 왜 안되지.. 이러는 바보같은 실수를...

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a, b = phone_book[i], phone_book[i+1]
        if len(a) <= len(b):
            if a == b[:len(a)]:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["123","124","1235","567","88"]))
print(solution(["34","35","3","3456","88"]))