def solution(gems):
    size = len(set(gems))  # 중복제거한 길이 - 구간이 최소가 되어야 하기 때문
    dic = {gems[0]: 1}
    temp = [0, len(gems) - 1]  # 구간을 담을 변수 - 마지막에 +1 해서 출력
    start, end = 0, 0  # 투포인터 설정

    while(start < len(gems) and end < len(gems)):

        # start 증가
        if len(dic) == size:  # 모든 보석이 각각 하나씩 나온 상황일때
            if end - start < temp[1] - temp[0]:  # 구간이 더 작다면, 최소구간 교체
                temp = [start, end]
            if dic[gems[start]] == 1:  # 빈도수가 0이면 dic에서 제거
                del dic[gems[start]]
            else:  # 빈도수 감소
                dic[gems[start]] -= 1
            start += 1  # start 증가

        # end 증가
        else:
            end += 1  # end: 끝 부분을 하나씩 늘리면서 구간 재산정
            if end == len(gems):  # 범위를 넘어가면 안되니까 끝에 도착하면 종료
                break
            if gems[end] in dic.keys():  # 보석이 이미 있으면 +1
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1  # 보석이 없으면 새롭게 추가

    return [temp[0]+1, temp[1]+1]
