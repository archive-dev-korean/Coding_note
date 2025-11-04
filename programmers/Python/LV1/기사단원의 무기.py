# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/136798

# 내 풀이 :
# 약수개의 구하는 로직에서 시간 복잡도가 O(N)이 되는데 결국 시간 초과로 틀린 코드였음

def solution(number, limit, power):
    answer = 0
    lst=[]
    for i in range(1, number+1):
        cnt =0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt >= limit:
            answer += power
        else:
            answer += cnt  
    return answer

# 결과는 나올 텐데 수가 커지면 시간이 오래걸림
# 시간 복잡도를 고려하여 제곱수 방법을 선택함

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        cnt = 0
        for d in range(1, int(i ** 0.5) + 1):
            if i % d == 0:
                cnt += 2
        if int(i ** 0.5) ** 2 == i:  # 완전제곱수면 중복 1개 빼기
            cnt -= 1
        # 여기서 i의 약수 개수 cnt가 확정됨
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer

# 내가 쓴 것과 다른건 약수 구하는 로직 밖에 없음
