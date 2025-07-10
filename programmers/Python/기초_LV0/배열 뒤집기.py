# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    answer = []
    for i in range(len(num_list) -1,-1,-1):
        answer.append(num_list[i])
    return answer

# 가장 보편적으로 생각하는 방식이지만

def solution(num_list):
    return num_list[::-1]
  
#   슬라이싱 쓰면 간단하단걸 알았다
# 활용법을 조금 더 생각해보자
