# 문제 : 문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    answer = ''
    for char in my_string:
        if char not in answer:
            answer += char
    return answer
#   이게 정석적인 풀이 인데 이해가 잘 안되었음 일단 생각하는 것도 못했고..
# answer는 처음엔 비어 있으니까 처음부터 값을 넣게 됨, 그러다가 중복되는 문자 나오면 if 조건 때문에 값을 안 넣게 됨


# 보다 간단한 풀이가 있긴 하다(딕셔너리와 fromkeys활용)
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
  # 딕서너리 fromkeys로 중복된 문자를 찾아서 리턴하면 된다.
