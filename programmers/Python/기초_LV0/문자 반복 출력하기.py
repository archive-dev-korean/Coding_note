# 문제 : 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 정석 풀이 
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer

# 간단한 풀이
def solution(my_string, n):
    return ''.join(i*n for i in my_string)
# 사실 리스트 컴프리헨션 쓴거다
