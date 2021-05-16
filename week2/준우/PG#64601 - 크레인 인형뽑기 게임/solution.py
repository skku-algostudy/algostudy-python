BLANK = 0


def solution(board, moves):
    n = len(board)
    answer = 0
    stack = []
    for move in moves:
        i = move - 1
        col = [row[i] for row in board]
        # print(move, col)
        for idx in range(n):
            if col[idx] != BLANK:  # 인형을 찾으면
                if len(stack) > 0 and stack[-1] == col[idx]:  # 스택과 함께 사라지던가
                    stack.pop()
                    answer += 2
                else:  # 스택에 어펜드해주던가.
                    stack.append(col[idx])
                board[idx][i] = BLANK  # s
                break  # 그 다음 Move로 넘어가야 할 것.
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
