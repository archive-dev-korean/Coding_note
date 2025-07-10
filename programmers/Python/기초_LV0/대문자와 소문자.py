# 문제 : 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.


# swapcase()쓰면 알아서 대소문자 자동으로 변환이됨
def solution(my_string):
    answer = my_string.swapcase()
    return answer



# 이게 정석 풀이 인데
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer

# swapcase()처음 써봐서 알아야겠다 생각해서 기록했음
