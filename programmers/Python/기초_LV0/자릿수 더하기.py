# 문제 : 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

def solution(n):
    answer=0
    while n > 0:
        answer += n%10
        n = n//10
    return answer
# 이게 정석적으로 python 스럽지 않게 푼 것 같다.

# 이거는 뭐 따로 간단하게 풀 방법이 크게 없는 것 같다.

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer

# 이게 수학적으로 정석 같다.
