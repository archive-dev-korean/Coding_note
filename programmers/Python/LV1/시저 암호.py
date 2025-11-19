# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12926

# 처음에 딕셔너리 만들어서 풀려다가 대문자, 소문자, 공백 모두 있는 걸 보고 포기
# 결국 아스키 코드 풀어서 해결하는 거라고 알게 됨
# 이 과정에서 chr() 과 ord() 도 알게됨
# chr() -> 정수를 문자로
# ord() -> 문자를 정수로

def solution(s,n):
  answer=''
  for i in s:
    if 'a'<= i <= 'z:
      answer+= chr((ord(i) - ord('a') +n ) % 26 + ord('a'))
    elif 'A' <= i <= 'Z':
      answer += chr(ord(i) - ord('A') +n) % 26 + ord('A'))
    else:
      answer+=i

return answer

# if 조건문이 n번 움직인 이후에 문자열을 반환 하는 것
# 'A' 의 아스키 코드 값은 65이기 때문에 %26 을 하면 원래 아스키 코드 값으로 돌아옴
