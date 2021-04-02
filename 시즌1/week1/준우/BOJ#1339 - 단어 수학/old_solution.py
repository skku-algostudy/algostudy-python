# if in dict -> 그대로 반영
# if not in dict -> 반영 X

word_n = int(input())
words = []
words_dict = {}
max_length = 0
answer = 0
alph_value = 9

for _ in range(word_n):
    word = input()
    if len(word) > max_length: # max_length엔 길이가 저장되게 될 것.
        max_length = len(word)
    words.append(word) # 현재 words는 스트링 형태

words.sort(key=lambda x:len(x), reverse=True)

print(words)
print(max_length)

for l in range(max_length, 0, -1): # max_length~1까지 반복
    current_i = max_length-l # 그 때 인덱스는 0~max_length가 되겠지.
    savepoints = []
    for word in words: # 각 단어마다
        if len(word) >= l: # 지금의 길이에 해당한다면
                if word[current_i] in words_dict: # 사전에 있으면 그 값을 반영해주고
                    answer += words_dict[current_i]
                else: # 사전에 없으면..
                    savepoints.append(words_dict[current_i])
    
    if savepoints: # 아 여기서부터 어떻게 접근하지?
        for i in 
        for each in savepoints: # 그 다음에 존재하는지 확인해야 할것.
            for word in words:
                if len(word) >= l:
                    if word[current_i+1] == each
                    
                    




