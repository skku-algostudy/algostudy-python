# 이 코드 또한 무엇이 문제일꼬..

def solution1(n, losts, reserves):
    lost_dict = {}
    for lost in losts:
        lost_dict[lost] = True

    for reserve in reserves:
        if reserve in lost_dict and lost_dict[reserve]:
            lost_dict[reserve] = False
        elif reserve-1 in lost_dict and lost_dict[reserve-1]:
            lost_dict[reserve-1] = False
        elif reserve+1 in lost_dict and lost_dict[reserve+1]:
            lost_dict[reserve+1] = False

    answer = n
    for each in lost_dict:
        if lost_dict[each]:
            answer -= 1

    return answer


def solution2(n, losts, reserves):
    lost_dict = {}
    for lost in losts:
        lost_dict[lost] = True

    for reserve in reserves:
        if reserve in lost_dict and lost_dict[reserve]:
            lost_dict[reserve] = False
        elif reserve+1 in lost_dict and lost_dict[reserve+1]:
            lost_dict[reserve+1] = False
        elif reserve-1 in lost_dict and lost_dict[reserve-1]:
            lost_dict[reserve-1] = False

    answer = n
    for each in lost_dict:
        if lost_dict[each]:
            answer -= 1

    return answer


def solution(n, losts, reserves):
    return max(solution1(n, losts, reserves), solution2(n, losts, reserves))
