# 문제 : my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120902

# 일단 처음에 내 방식대로 풀었을 떄,
def solution(my_string):
    my_string = my_string.split()
    answer = 0
    for i in my_string:
        if i == '+':
            answer += int(i)
        else:
            answer -= int(i)
            
    return answer
  # 이렇게 풀었었는데 아이디어는 어느정도 맞았으나 개발 능력이 부족해서 실행되지 않았음

  # 그래서 
  # 조금 수정한 코드가 
  def solution(my_string):
    my_string=my_string.split()
    answer = int(my_string[0])
    for i in range(1, len(my_string), 2):
        cal = my_string[i]
        num = int(my_string[i+1])
        if cal =='+':
            answer += num
        else:
            answer -= num
    return answer   

# 이거다 answer를 my_string에서 처음 값으로 주고 연산기호는 어짜피 한수 걸러 한수 사이에 나오기 떄문에 range()값에서 step을 2로 줘서 기호만 따로 구한다
# 그다음 연산 기호 다음 수를 num으로 지정한다. 연산기호가 나오면 알맞은 연산을 해서 answer에 num을 연산한다.

# 하지만 eval로 푼 사람도 있다.
def solution(my_string):
   return eval(my_string)

# 흠. 이게 좋은건지 모르겠다. 실무에서는 잘 안쓰는걸 추천하지만 코딩테스트 에서는 써도 되나?
  
