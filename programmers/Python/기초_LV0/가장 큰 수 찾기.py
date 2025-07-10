# 문제 : 정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    # answer = []
    for i, j in enumerate(array):
        if max(array) == j:
            return [j,i]
# 정석 풀이 이다. 하지만 조금 더 변형하면

def solution(array):
    return list[j,i for i,j in enumerate(array) if j == max(array)]
# 이렇게 풀 수도 있다.
