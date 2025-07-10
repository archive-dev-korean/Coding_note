# 문제 : 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주

def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] not in ('a','e','i','o','u'):
            answer += my_string[i]
    return answer
# 가장 정석적이고 python 스럽지 않은 풀이 같다
# 간편하게 푸는 다양한 방법이 있지만

def solution(my_string):
  return ''.join([i for i in my_string if not(i in "aeiou")])

# 이렇게 푸는게 좋다. 리스트 컴프리헨션 과 join 메서드 쓰면 된다.
# 이떄 문제를 풀면서 리스트 컴프리헨션을 처음 사용해 본 것 같다.
