# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    for i in range(len(t) -m +1):
        
        if int(t[i:i+m]) <= int(p):
            answer+=1
    return answer

# 처음에 for 문 범위랑 슬라이싱 범위가 이해가 잘 안되었는데 직접 몇가지 경우 대입해 보니까 조금 알겠다
