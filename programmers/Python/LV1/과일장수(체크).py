# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/135808

# 일단 내 풀이 : 
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    # slice=score[::m]
    for i in range(0, len(score), m):
        if i >= k:
            i = k
        elif len(score) % m > 0:
            m = (len(score) // m) 
            
        answer += i * m
        
    
    return answer

# 이렇게 풀다가 elif 주석 처리하고 돌리니까 테스트 케이스에서 하나 맞췄는데 그래서 elif조건만 잘 수정하면 될 수도 있겠다 생각함
# 그런데 로직이 조금 이상해 지는 것 같아서 조언을 보니

def solution(k, m, score):
    score.sort(reverse=True)  # 내림차순
    answer = 0
    for i in range(m - 1, len(score), m):
        answer += score[i] * m
    return answer
  # 이렇게 쉽게 작성할 수 있었음.........
  # m개씩 꽉 찬 박스만 계산: 인덱스 m-1, 2m-1, 3m-1 ... 가 각 박스의 최저 점수 위치
