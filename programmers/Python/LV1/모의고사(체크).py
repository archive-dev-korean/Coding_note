# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/42840

# 일단 완전탐색 알고리즘 쓰는 거라고 정해져 있음

# 각각 의 정답 마다 각 패턴별로 자릿수와 정답을 비교하면 점수가 나오고 최대 점수도 마찬가지로 구할 수 있음
# 나도 여기까지는 생각했는데 어떻게 구현하는 건지 몰랐음
# 정답을 보고 여러 가지 찾아보니

# p1[i & len(p1)] 이런 방식으로 하면 순서대로 모든 수를 패턴과 일치 하는지 확인 할 수 있다는 것을 꺠달았음...
# 이게 완전탐색 알고리즘

def solution(answers):
  # 수포자들이 찍는 패턴
  p1 = [1, 2, 3, 4, 5]
  p2 = [2, 1, 2, 3, 2, 4, 2, 5]
  p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

  score1 = 0
  score2 = 0
  score3 = 0

  # 각각의 정답과 패턴을 비교 (완전탐색)
  for i in range(len(answers)):
      ans = answers[i]

      # 1번 수포자
      if ans == p1[i % len(p1)]:
          score1 += 1

      # 2번 수포자
      if ans == p2[i % len(p2)]:
          score2 += 1

      # 3번 수포자
      if ans == p3[i % len(p3)]:
          score3 += 1

  # 최고 점수 찾기
  max_score = max(score1, score2, score3)

  result = []
  if score1 == max_score:
      result.append(1)
  if score2 == max_score:
      result.append(2)
  if score3 == max_score:
      result.append(3)

  return result
