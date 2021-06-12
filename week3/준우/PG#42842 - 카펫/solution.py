def get_brown_n(xn: int, yn: int):
    return (xn + 2) * 2 + yn * 2


def solution(brown: int, yellow: int) -> list:
    for yellow_yn in range(1, int(yellow**0.5) + 1):
        # 나누어 떨어지지 않으면 컨틴뉴
        if yellow % yellow_yn != 0:
            continue

        yellow_xn = yellow // yellow_yn
        if get_brown_n(yellow_xn, yellow_yn) == brown:
            return [yellow_xn + 2, yellow_yn + 2]
