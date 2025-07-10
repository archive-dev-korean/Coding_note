# 문제 : 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    for i in range(len(numbers)):
        sum += i
        return sum / len(numbers)
    # answer = 0
    # return answer

# 초반에 코드를 이렇게 썼었는데 완전히 잘못 썻고

def solution(numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)
  # 이렇게 수정했다가 

def solution(numbers):
    return sum(numbers) / len(numbers)
  # 이렇게 쓰면 간단한걸 꺠달았다 생각하는 능력을 좀더 길러야 할 것 같다.
