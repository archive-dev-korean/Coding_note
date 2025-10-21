출처 : https://school.programmers.co.kr/learn/courses/30/lessons/178871

풀이1(딕셔너리사용) : 
def solution(players, callings):
  pos = {name: i for i, name in enumerate(players)}
    for name in callings:
        i = pos[name]
        if i ==0:
            continue
        front = players[i - 1]

        players[i - 1], players[i] = players[i] , players[i-1]

        pos[name] = i -1
        pos[front] = i
    return players

풀이2(인덱스 사용) :
def solution(players, callings):
  for name in callings:              # 불린 이름 하나씩 순서대로 처리
      i = players.index(name)        # 현재 순위(인덱스) 찾기
      players[i - 1], players[i] = players[i], players[i - 1]  # 앞사람과 자리 바꿈
  return players

오답:
#     for i,j in enumerate(players):
#         if j == callings[i]:
#             answer.append(players[i-1])


자리 바꾸기 생각 안함
