# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/138477

# 원래 이중 for문으로 접근해서 풀려고 했음
def solution(k,score):
  answer=[]
  for i in range(len(score)):
    for j in score[i:k]:
      answer.append(i)
      answer.sort(reverse=True)
      return answer
# 이렇게 풀고 있다가 테스트 보니까 뭔가 잘못 저장 되고 있었음
# 그래서 if 문 추가해서 하는 건가 생각해보니까 그렇게 하면 안될 것 같아서
# 다른 방식으로 생각함

for i in range(len(score)):
  temp=[]
  for j in range(i+1):
    temp.append(score[j])
  temp.sort(reverse=True)
  answer.append(temp[min(i, k-1)])
return answer

# 근데 이렇게 짜면 효율이 떨어짐

# 가장 효율적인 코드는
   answer = []
   hall =[] # 추가된 항목
   for i in score:
        answer.append(i)
        answer.sort(reverse=True)
        if len(answer) > k:
            answer.pop()            # k개만 유지
        hall.append(answer[-1])
    return hall
# 이 코드인데 단일 for 문이고 k개만 유지한다는 조건 때문에 가장 효율적인 코드이고 pop()과 -1을 이용해서 최솟값만 빼온다
