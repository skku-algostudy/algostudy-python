# 아니 이 방법이 안된다고?

def get_point(n):
    jaritsu = len(str(n))
    return (n * (10 ** (4-jaritsu)), -jaritsu)


def solution(ns):
    ns.sort(key=get_point, reverse=True)
    return ''.join(map(str, ns))


print(get_point(6))
print(get_point(10))
print(get_point(2))
print(get_point(1))
print(get_point(50))
print(get_point(5))
print(solution([6, 10, 2, 1, 5, 50]))
