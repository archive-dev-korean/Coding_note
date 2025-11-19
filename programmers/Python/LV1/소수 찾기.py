# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12921

# 내가 푼 방식은 루트n까지만 반복해서 소수 판별하는 코드 
def solution(n):
    answer = 0
    for i in range(2, n+1):
        result = True
        for j in range(2, int(i**0.5) + 1):
            if i % j ==0:
                result=False
                break
                
        if result:
            answer+=1
    return answer 

# 뭐 틀린건 아니지만 소수판별할 때는 에라토스테네스의 체 사용하는게 가장 전형적인 방법임

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
#   이렇게 처음 봤을 때 한번에 보고 이해하기 어려웠지만 훨씬 효율이 빠르다.

# 가장 표준이 되는 에라토스테네스의 체 코드는 아래와 같음
def solution(n):
    sieve = [True] * (n + 1)      # 처음엔 모두 소수(True)라고 가정
    sieve[0] = sieve[1] = False   # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):  # i의 배수들을 False로 변경
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i]]  # 소수 리스트 반환

# 이걸 변형해서 만든게 두번 째 코드임

  
