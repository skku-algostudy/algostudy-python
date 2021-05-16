# def solution(numbers, hand):
#     l_hand, r_hand = 10, 12
#     answer = ""

#     for number in numbers:
#         if number in [1,4,7]:
#             answer += "L"
#             l_hand = number

#         elif number in [3,6,9]:
#             answer += "R"
#             r_hand = number

#         else: # 중간 숫자
#             number = 11 if number == 0 else number # n이 0일때는 n을 11로 생각

#             abs_l = abs(number - l_hand)
#             abs_r = abs(number - r_hand)

#             if sum(divmod(abs_l, 3)) > sum(divmod(abs_r, 3)):
#                 answer += "R"
#                 r_hand = number

#             elif sum(divmod(abs_l, 3)) < sum(divmod(abs_r, 3)):
#                 answer += "L"
#                 l_hand = number

#             else:
#                 if hand == "left":
#                     answer += "L"
#                     l_hand = number
#                 else:
#                     answer += "R"
#                     l_hand = number


#     return answer

# -- 아이디어 생각 O
# -- 중간 숫자에 대한 계산 부분만 신경쓰면 되는 문제
def solution(numbers, hand):
    answer = ''
    lastL = 10
    lastR = 12

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            lastL = n
        elif n in [3, 6, 9]:
            answer += 'R'
            lastR = n
        else:
            n = 11 if n == 0 else n

            absL = abs(n-lastL)
            absR = abs(n-lastR)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                lastR = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                lastL = n
            else:
                if hand == 'left':
                    answer += 'L'
                    lastL = n
                else:
                    answer += 'R'
                    lastR = n

    return answer
