# 문제 : 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120864

# 처음에 
def solution(my_string):
    answer = 0
    # digits =''.join([c for c in my_string if c.isdigit()])
    # print(digits)
#   이렇게 구하면 자릿수 계산이 안됨

# 그래서 정규식 안쓰고 싶지만 정규식 사용할 수밖에 없었음

import re
def solution(my_string):
    answer = 0
    numbers = re.findall(r'\d+',my_string)
    answer = sum(int(num) for num in numbers)
    return answer

# 정규식을 잘 몰라서 찾아본 것이 단점임 게다가 numbers는 리시트로 저장된다는 걸 알아야 했음 다음부터는 꼭 알고서 작성하기

# 그래서 더 간단하고 직관적인 코드를 찾음
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

# 아 좀만 더 생각했으면 여기까지 할 수 있었을 것 같은데 아쉬움
