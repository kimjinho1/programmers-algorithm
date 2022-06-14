def solution(board, moves):
    ans = 0
    stack = []
    for m in moves:
        for i in range(len(board)):       
            if board[i][m-1]:
                stack.append(board[i][m-1])
                board[i][m-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(); stack.pop()
                        ans += 2
                break
                
    return ans