# 문제 : 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요

def solution(numbers):
    max = float('-inf')
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            product = numbers[i] * numbers[j]
            if product > max:
                max = product
    return max

# 복잡하게 풀면 이렇게 푼다(매우 비추)

def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
# 간단하게 풀면 이렇게 푼다. sort() 사용하면 자동으로 오름차순 정렬된다.
# sort() 알고 기억하라고 적어둔다.
