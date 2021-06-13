# 2개의 숫자를 비교해서 작은 것을 제거
# 문자 제거 : replace 함수 사용
# 리스트로 접근하는 것이 편할 듯

'''def solution(number, k):
    reduce_num = 0 # 제거한 숫자 개수
    str_num = list(number)
    while reduce_num != k:
        idx=1; left=0; right=2
        #1. 본인을 기준으로 좌우와 크기 비교 (맨앞 3개의 숫자 비교)
        #2. 작은 수 제거
        #1-1. 왼쪽이 더 작은 경우 (i-1)
        if str_num[idx] > str_num[left]: str_num.pop(left)     
        #1-2. 오른쪽이 더 작은 경우 (i+1)
        elif str_num[idx] > str_num[right]: str_num.pop(right)
        #1-3. 본인이 제일 작은 경우
        else: str_num.pop(idx)
        print(str_num)
        reduce_num+=1
    print(str_num)
    return ''.join(str_num)'''


def solution(number, k):
    collected = []  # 숫자를 모아서 큰 수를 만들 때 쓰일 배열
    # 문자열에도 모을 수 있지만 문자열은 immutable(값이 변하지 않는)특성을 가지기에 코드 효율은 리스트(mutable)다 더 좋다
    # call by value , call by reference와 동일한 개념
    for i, num in enumerate(number):
        # k개 만큼의 숫자를 빼냈을 때, i의 인덱스를 기억하기 위해서 i를 사용
        while len(collected) > 0 and collected[-1] < num and k > 0:
            # 1. 맨 마지막 문자만 비교를 하면 될까? -> 그렇다. 지금까지 원칙을 지켜서 쌓아 왔다면 지금까지 쌓인 숫자들은 내림차순으로 되어있다.
            # 2. collected의 마지막 원소는 한 문자로 이루어진 문자열이다. num 또한 한 글자 짜리 문자열이다. 이걸 정수로 변환하지 않고,
            # 두개의 문자열에 대해서 대소관계를 이용해도 괜찮은가? -> 괜찮다. 알파벳 순서에 따르면 0은 1보다 작고, 3은 2보다 크고, 수의 크기 대소관계와 같다.
            # ※ 길이가 2 이상이라면, 사전에 나타난 숫자가 되겠지만, 지금은 한글자 짜리기 때문에 정수 변환이 필요없다.
            collected.pop()  # 리스트이 맨 끝에 있는 원소 하나를 없앤다.
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
    # k가 0 이면 빈 리스트가 되기 때문에 if를 이용해서 조건을 걸어준다.
    answer = ''.join(collected)
    return answer


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
