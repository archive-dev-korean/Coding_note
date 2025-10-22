출처 : https://school.programmers.co.kr/learn/courses/30/lessons/161990

나는 행,열 따로 따로 순회해서 적으려고 헀는데 그 방식
:

def solution(wallpaper):
    answer = []
    
    H = len(wallpaper) #x 좌표 세로
    W = len(wallpaper[0]) # y좌표 가로
    
    min_i, min_j = H , W 
    max_i, max_j = -1, -1
    
    for i in range(H):
        for j in range(W):
            if wallpaper[i][j] == '#':
                if i< min_i: min_i =i
                if j< min_j: min_j =j
                if i> max_i: max_i =i
                if j> max_j: max_j =j
                # answer.append(min_i,min_j, max_i+1, max_j+1)
    return [min_i, min_j, max_i + 1, max_j + 1]


근데 간단한 방식이 있음
def solution(wallpaper):
    a=[]
    b=[]
    for i, name in enumerate(wallpaper):
        for j, name2 in enumerate(name):
            if name2 == '#':
                a.append(i)
                # if name2 == '#':
                b.append(j)
    return [min(a),min(b),max(a)+1,max(b)+1]


일단 최대 최소 로직은 처음 짤 때 생각못하고 짬 ㅜ
