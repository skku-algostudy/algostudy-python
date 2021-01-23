
# 그리디 알고리즘은 항상 최적의 해를 제공하지 않는다.

# 현재 시점에서 최적의 답을 찾기 위한 방법
# 그리디 알고리즘이 가장 적합한 방법이라는 근거를 찾아내야 한다.

# [참조] velog.io/@kyle/그리디-알고리즘Greedy

# 우선적으로 5단계의 단계에 따라 러프하게 문제를 접근해보겠습니다 :)
# 1. 문제의 가장 핵심적인 포인트 한가지 뽑아보기
# - 1.1 그에 따라 신경써야하는 조건을 나열한다.
# 2. 그 포인트를 어떤 방식(조건/알고리즘)으로 해결할 수 있는가?
# 3. 플로우 생각해보기
# 4. 구현 방식 생각해보기 (수도 코드, 구현 아이디어 등)
# 5. 실제코드 작성

# 1. 문제
# (핵심) 단어(->숫자)를 더할때 그 수의 합이 최대가 되어야 함.
# (다른 말) 단어를 숫자로 변환할때 최대값이 되어야 한다.

# 1.1 세부조건
# - 각 단어는 알파벳 대문자 (A ~ Z)
# - * 알파벳은 '0 ~ 9' 숫자로 변환할 수 있음
# - 숫자는 한번씩만 사용가능

# 2. 포인트 - 해결 아이디어
# - 최대가 되려면???
# --- 자릿수가 큰 부분부터 큰 값을 부여하면 되지 않을까?
# --- ex) GCF + ACDEB 의 경우 ACDEB가 자릿수가 더 크기 때문에
# --- A부터 9 , C에게 8 ... 다음은 G에게 7 또는 D에게 7가능
# --- 큰 순서대로 A C G D E F B
# --- 큰 순서대로 9 8 7 6 5 4 3
# 784 + 98653
# 99437
# ---- ** 자릿수의 합은 순서에 관계없기 때문에 그냥 차례대로 부여하면 될 것이다.

# 3. 플로우
# 자릿수에 맞게 숫자 부여를 어떻게 하지???
# 자릿수를 어떻게 파악하지???

# 4 구현 방식
# --- 구현 방식에서 막혔습니다... 많이 고민했는데 풀이가 막히네요...
# --- 블로그 참고하겠습니다.
# --- 출처: https://hjp845.tistory.com/129
# --- 딕셔너리를 사용하라는 아이디어
# --- 자릿수는 각 위치에 맞게 10의 배수를 곱해주는 아이디어


# 입력값들
words = []
n = int(input())
for _ in range(n):
    words.append(input())


def solution(n, words):

    # variables
    word_sum = 0
    alphabet_priority = [0 for i in range(26)]

    for word in words:
        exp = 0
        while word:
            alphabet = word[-1]
            # ** > pow()
            alphabet_priority[ord(alphabet) - ord('A')] += pow(10, exp)

            exp += 1
            # 슬라이싱 or index ?
            word = word[:-1]

    alphabet_priority.sort(reverse=True)

    for i in range(9, 0, -1):
        word_sum += i * alphabet_priority[9 - i]

    print(word_sum)


solution(n, words)
