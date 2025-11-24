# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12933

# 정수를 문자열로 바꿔서 정렬하고 다시 정수 방식으로 전환해서 품
def solution(n):
    # answer = 0
    answer=sorted(str(n),reverse=True)
    jk=int("".join(answer))
    return jk

# 알아둬야 할 건 정수를 문자열로 바꿀 때, 어떻게 바꾸냐임
# str(n)이렇게 쓰면 되는데

# 다시 정수형으로 바꿀땐, int("".join(answer))이렇게 앞에 정수형 자료형 입력해주고 "".join(answer)이렇게 쓰면 됨
