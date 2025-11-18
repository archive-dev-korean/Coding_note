# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12977

# 소수 구하는 로직을 2이상에서 1과 자기자신을 약수로 가지는 수 라는 정의를 이용해 구했음
def solution(nums):
    answer = 0
    cnt=0
    def sosu(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:  # 하나라도 나눠떨어지면 소수 아님
                return False
        return True
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                answer = nums[i]+nums[j]+nums[k]
                if sosu(answer):
                    cnt += 1
    return cnt
# 함수로 만들어서 그리고 삼중 for문 으로 3가지 원소 골라서 합한 다음 조건에 부합하는지 테스트 
# 이렇게 하는 것보다 간편한 방법이 있음

from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

def solution(nums):
    count = 0
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            count += 1
    return count

# combination 함수를 쓰면 3개 알아서 뽑아주니까 더 잘 구할 수 있음 소수 판별도 제곱근만 확인하면 되기 때문에 더 간편함
