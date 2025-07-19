# 문제 : 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120846

def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        count = 0
        for j in range(1,i+1):
            if i % j ==0:
                count+= 1
        if count >=3:
            answer+=1
    return answer

# 이렇게 푸는게 정석이면서 가장 깔끔한 것 같다. 일단 합성수 구하는 것 부터 가독성이 좋고, 람다식 쓰는 것보다 그렇게 줄이 길지도 않다.
