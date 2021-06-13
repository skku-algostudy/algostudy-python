''' 문자열은 정렬이 Set '''

# 앞자리 숫자가 큰 게 앞에 올 수록 숫자가 커진다. 자릿수비교. 문자열의 대소비교가 포인트

# 순열로 가장 긴 길이의 숫자를 만들고 max() 이용

# (예제만 통과)
# def solution(numbers):
#     import itertools
#     number_string = list(map(''.join, itertools.permutations(numbers)))
#     number_string = map(int, number_string)
#     return str(max(number_string))


def solution(numbers):
    numbers = list(map(str, numbers))  # 원소를 문자열로 변환
    numbers.sort(key=lambda x: x*4, reverse=True)  # 자릿수비교 위해 x*4 이용
    '''예제2
    333 303030 343434 555 999
    문자열의 대소비교는 맨 앞 부터 아스키코드값을 대소비교한다.'''
    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
