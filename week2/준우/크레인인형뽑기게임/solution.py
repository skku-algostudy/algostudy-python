'''
** input **
board : 이차원 알지?
moves : 어디어디 들어올릴지

** output ** 
그러면 몇 개가 터졌을까?

** 유의점 **
같은 두 개 만나면 터진다 -> 어떤 게 들어갔는지 기록해둬야함.

-- else를 써서 좋은 점 --
** if는 단발성인 반면 else를 쓰면 놓치는 경우를 한 번 생각할 수 있다. ** 
너무 간단하게 하려고만 하지 말자!

'''

def solution(board, moves):
    baguni = []
    answer = 0
    
    for move in moves: # 각 움직임마다
        for c in board: # 0~4까지
            if c[move-1] != 0: # 인형이 있다면
                baguni.append(c[move-1]) # 일단 바구니에 넣고
                
                if len(baguni) >= 2: # 두 개 이상 들어간 상황에서
                    if baguni[-2] == baguni[-1]: # 겹친다면 팝 팝 추가
                        baguni.pop(-1)
                        baguni.pop(-1)
                        answer += 2
                        
                c[move-1] = 0 # 뽑은 인형은 0 처리
                break 
    return answer 