# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/132267

# 내가 생각한 논리인데 
def solution(a, b, n):
    answer = 0
    while n >= a:
        mock = n // a
        n -= mock * a
        n += mock * b
        answer += mock * b
    return answer

# 원래는 
def solution(a, b, n): 
  answer = 0  
  while True:
    mock = (n // a)
    n -= (mock * a) 
    answer += mock 
  return answer
# 이런식으로 적었었는데 이러면 남은 콜라 계산이 잘 되지 않아서 문제가 생긴다.
# 여기서 n += mock * b의 값을 더해줘야 하는데 그걸 못했다 그리고 True여서 무한루프 계속 돔 시간 초과로 실패함
