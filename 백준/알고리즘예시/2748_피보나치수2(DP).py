# 동적 프로그래밍 예시 문제
# 시도1 Top - Down 방식(재귀)
cache =[-1] * 91
cache[0] =0
cache[1] =1
cnt=0 #함수가 얼마나 호출되는지 파악하기 위한 변수
# def f(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
    
#     return f(n-1) + f(n -2)

# 메모이제션 적용
def f(n):
    global cnt
    cnt+=1
    if cache[n]==-1:
        cache[n] = f(n-1) + f(n -2)
    #     return 0
    # elif n==1:
    #     return 1
    
    return cache[n]
print(f(int(input())))
# print(cnt)
# 메모이제이션 안써서 수가 커지면 계속 함수가 호출됨 (엄청 오래 걸림)
# 메모이제이션 적용 -> 리스트


#시도2 Bottom - UP 반복문으로 풀기
N=int(input())
cache=[-1] * 91
cache[0] = 0
cache[1] = 1

for i in range(2, N+1):
    cache[i] = cache[i-1] + cache[i-2]
print(cache[N])

# Top - Down 방식은 원하는 값만 따로 정의해서 원하는 범위만 구할 수 있어서 조금 더 쉬울 수도 있음