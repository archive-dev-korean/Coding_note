# 문제 : 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120844

# 정답 1(수작업, 슬라이싱) : 
def solution(numbers, direction):
    if direction == 'right':
        return [numbers[-1]] + numbers[:-1]
    else:  # direction == 'left'
        return numbers[1:] + [numbers[0]]

# 정답2(pop/insert 사용) : 
def solution(numbers, direction):
    if direction == 'right':
        last = numbers.pop()
        numbers.insert(0, last)
    else:
        first = numbers.pop(0)
        numbers.append(first)
    return numbers

# 정답3(deque와 rotate 사용 제일 추천):
def solution(numbers, direction):
    d = deque(numbers)
    if direction == 'right':
        d.rotate(1)
    else:  # direction == 'left'
        d.rotate(-1)
    return list(d)  

# 여기서 처음 pop과 insert, deque, rotate 사용해본것 같다. 관련 개념 정리하고 와야겠따.
