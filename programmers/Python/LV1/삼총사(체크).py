# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131705

# 내 풀이 (3중 for 문):
def solution(number):
  answer=0
  for i in len(number):
    for j in len(number):
      for k in len(number):
        if i + j +k ==0:
          answer+=1
    return answer

# 이런식으로 썼다가 이상해서
for i in range(len(number):
  for j in range(len(number)-i):
    for k in ragne(len(number)-j):
      # 이런식으로 바꿨었는데 이것도 이상해서 찾아보니

for i in range(len(number) -2):
  for j in range(i+1, len(number) -1):
    for k in range(j+1, len(number)):
      if number[i]+number[j]+number[k] ==0:
        answer+=1
  return answer
  # 이렇게 쓰면 맞는다 for 문 쓸때 end값의 범위와 start값만 정해주면 잘 돌아가는데 이걸 왜 생각해내지 못할까

  # Combination을 쓰는 방법도 있다
  def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt

# 제일 쉽다 라이브러리만 알고 있으면
