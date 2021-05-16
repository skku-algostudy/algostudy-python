def solution(user_id, banned_id):
    answer = 1
    for banid in banned_id:
        available = {}
        n = len(banid)
        for userid in user_id:
            if n == len(userid):
                available[userid] = True
        for i in range(n):
            if banid[i] == '*':
                continue
            for each in available:
                if banid[i] != each[i]:
                    available[each] = False
        temp = 0
        for each in available:
            if available[each]:
                temp += 1
        answer *= temp
    return answer


print(solution(["frodo", "fradi", "crodo",
                "abc123", "frodoc"], ["fr*d*", "abc1**"]))
