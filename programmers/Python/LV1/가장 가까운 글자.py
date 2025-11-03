# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/142086

# 딕셔너리를 사용한 최신 위치 저장 로직으로 풀어야 함.
def solutions(s):
  answer=[]
  point={}
  for i,j in enumerate(s):
    if j in point:  # j값 즉 문자열의 원소를 딕셔너리에 저장
      answer.append(i - point[j]) 
    else:
      answer.append(-1) #첫번째 원소는 무조건 없으니 -1값 저장
    point[j] = i #딕셔너리에 적용된 원소들의 위치값을 가장 최신으로 바꿈 answer.append(i - point[j])에서 그 저 문자열이랑 비교했을 때 가장 최신 위치 리턴함


    
    
    
