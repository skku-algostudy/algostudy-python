def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        apchuk = ''
        prev = s[:step]
        count = 1 # 애초에 1부터 들어가니까 count를 0이아닌 1부터 줬구나.
        for j in range(step, len(s), step): # 어차피 마지막은 무시되니까, step에서 step씩 쭉 가는것도 좋겠다.
            if s[j:j+step] == prev: # 지금 처리하는게 이전거랑 겹치면
                count += 1 # 카운트 하나 쌓고
            else: # 안겹친다면
                apchuk += str(count) + prev if count >= 2 else prev  # 2넘으면 숫자까지 1이면 그냥
                prev = s[j:j+step] # prev & count 재세팅
                count = 1
        apchuk += str(count) + prev if count >= 2 else prev # 후처리 또한 같은 논리로 깔끔하게
        answer = min(answer, len(compressed)) # 크으
    return answer