# 출처 : https://github.com/archive-dev-korean/Coding_note/new/main/programmers/Python/LV1

def solution(board, h, w):
    answer = 0
    n = len(board)
    dh = [0, 1, -1, 0]
    dw = [1, 0 ,0 ,-1]
    
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                answer +=1
    return answer

# 가이드 라인 따라서 풀었는데 다른 방식으로 풀 수 있는 방법 생각해야 겠음
