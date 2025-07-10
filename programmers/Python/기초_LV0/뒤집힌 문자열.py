# 문제 : 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요

def solution(my_string):
    answer = ''
    for i in range(len(my_string) -1,-1,-1):
        answer += my_string[i]
        
    return answer

# 정석적으로 풀면 이렇게 푸는게 맞는 것 같다. python적 사고가 좀 부족한 것 같이 이러면

def solution(my_string):
    return my_string[::-1]
  # 이렇게 써야 파이썬적 사고, 그리고 문자열도 슬라이싱 가능하다
