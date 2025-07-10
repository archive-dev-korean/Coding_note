# 문제 : 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

# 수학적 머리가 조금 부족한데 
# 정석풀이는 

def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i ==0:
            answer.append(i)
    return answer

# 이거다 

# 하지만 약간 변형해서 이렇게 풀 수도 있다.
def solution(n):
    answer = []
    return [i for i in range(1, n+1) if n % i ==0 ]

# 약수구하는 방법이 떠오르지 않아서 외워 버리자 그냥 
