# 키패드 : ri
r_nums = {3: 0, 6: 1, 9: 2}
l_nums = {1: 0, 4: 1, 7: 2}
m_nums = {2: 0, 5: 1, 8: 2, 0: 3}


def get_dist(loc1, loc2):
    r1, c1 = loc1
    r2, c2 = loc2
    return abs(r1-r2) + abs(c1-c2)


def solution(nums, hand):
    l_loc, r_loc = (3, 0), (3, 2)
    answer = []
    for num in nums:
        if num in r_nums:
            answer.append('R')
            r_loc = (r_nums[num], 2)
        elif num in l_nums:
            answer.append('L')
            l_loc = (l_nums[num], 0)
        else:
            loc = (m_nums[num], 1)
            r_dist, l_dist = get_dist(loc, r_loc), get_dist(loc, l_loc)
            if r_dist < l_dist:
                answer.append('R')
                r_loc = (m_nums[num], 1)
            elif r_dist > l_dist:
                answer.append('L')
                l_loc = (m_nums[num], 1)
            elif hand[0] == 'l':
                answer.append('L')
                l_loc = (m_nums[num], 1)
            elif hand[0] == 'r':
                answer.append('R')
                r_loc = (m_nums[num], 1)

    return ''.join(answer)


print(solution())
