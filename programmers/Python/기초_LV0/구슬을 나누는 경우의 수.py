# 문제 : 머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다. 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120840

# 콤비네이션을 구하는 로직을 만들면 된다. balls C share 이렇게
# 일단 팩토리얼로 각각 구하려고 했다

def solution(balls, share):
  a, b =1
  for i in range(1, share+1):
    a *= balls
    balls -= 1
    b *=i
  return int(a/b)

# 이렇게
# 근데 간단하게 팩토리얼 함수 쓰면 조금더 명확한 것 같아서
import math
def solution(balls, share):
    answer = 0
    i = 1
    b=math.factorial(balls)
    a=math.factorial(balls-share)
    c=math.factorial(share)
    answer = b // (a*c)
    return answer

# 이렇게 했다.
# * 참고로 콤비네이션 함수도 math 라이브러리에 있다고 한다.
import math
def solution(balls, share):
  return math.comb(balls, share)

# 이렇게
