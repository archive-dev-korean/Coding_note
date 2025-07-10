# 문제 : 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# 처음에 람다식 써서 풀려고 하다가 실패
def solution(numbers):
    answer = map(lambda x: x*(x-1), numbers)
    # answer=[x*y for x,y in numbers]
    return max(answer)

# 튜플이 필요해 보여서 실패

# 정렬과 리스트 컴프리헨션으로 보다 쉽게 구할 수 있음

#정렬을 사용한 방법
def solution(numbers):
    numbers.sort()
    return max(numbers[-1]*numbers[-2],numbers[0]*numbers[1])

# for문 사용 이중 for 문
def solution(numbers):
    return max([a * b for i, a in enumerate(numbers) for j, b in enumerate(numbers) if i != j])

# 여기서 enumerate()는 range(len(리스트))와 같음
