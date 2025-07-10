# 문제 : 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

  def solution(my_string, num1, num2):
    answer =''
    for i, j in enumerate(my_string):
        if i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
        else:
            answer += my_string[i]
    return answer
# 가장 정석 풀이다.

# 이건 형변환을 사용해서 푼 방식인데 이건 생각하기 좀 어려운 것 같다.
def solution(my_string, num1, num2):
    str_list = list(my_string)          # 문자열 → 리스트로 변환
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]  # swap
    return ''.join(str_list)            # 리스트 → 문자열로 다시 합침
