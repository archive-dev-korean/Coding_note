# 문제 : 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120852

# 일단 math 라이브러리를 써볼까? 하다가 쓴다면 조건을 어떻게 적여야 할지 부터 막혔다.
import math
def solution(n):
    answer = []
    if math.sqrt(n) 
    return answer
# 일단 써보고 막혀서 다른 방법 선택

def solution(n):
    answer=[]
    i = 2
    while i*i <= n:
        if n % i ==0:
            answer.append(i)
            n //= i
        else:
            i += 1
    if n>1:
        answer.append(n)
    return sorted(list(set(answer)))

# 결국 정답은 이건데 생각조차 하지마 못함..
# set으로 중복 제거할 생각도 못했고, while 루프를 저렇게 조건을 줘서 돌게 할지도 생각못함.. 
# n //= i로 계속 나눠지니까 다시 while 돌 때는 i로 나눠진 수를 검사하기 때문에 인수분해 가능.
# 마지막으로 나눠지지 않을 때는 자기자신이 소수여서 리스트에 담고

