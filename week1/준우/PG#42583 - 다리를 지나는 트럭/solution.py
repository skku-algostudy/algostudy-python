from collections import deque


def solution(bride_length, weight, truck_weights):
    remaining_truck_n = len(truck_weights)
    trucks = deque(enumerate(truck_weights))
    truck = trucks.popleft()
    bride_dict = {truck: 0}
    time_elapsed = 0
    bride_weight = truck[1]

    while remaining_truck_n > 0:
        to_pop = []
        for truck in bride_dict:  # 이 반복문 안에서 pop해버리면 dictionary size 바뀌었다고 에러뜸.
            bride_dict[truck] += 1
            if bride_dict[truck] > bride_length:
                to_pop.append(truck)
        for truck in to_pop:
            print(f'{truck} 탈출')
            bride_dict.pop(truck)
            bride_weight -= truck[1]
            remaining_truck_n -= 1
        if trucks and trucks[0][1] + bride_weight <= weight:  # 차를 올릴수있다면 올려주고
            truck = trucks.popleft()
            bride_weight += truck[1]
            bride_dict[truck] = 0
            print(f'{truck} 들어감')
        time_elapsed += 1
        print(f'지금까지 {time_elapsed}초 경과, 다리:{bride_dict}')
        # 모든 다리의 트럭들의 시간을 1씩 늘려주고, 다 지났으면 팝

    return time_elapsed


print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
