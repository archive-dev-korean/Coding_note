# 문제 : 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120894

# 일단 딕셔너리 써서 푼다.
def solution(numbers):
    answer = 0
    dict={'zero':'0',
        'one':'1',
         'two':'2',
         'three':'3',
         'four':'4',
         'five':'5',
         'six':'6',
         'seven':'7',
         'eight':'8',
         'nine':'9'}
    for i,j in dict.items():
        numbers = numbers.replace(i,j)
    return int(numbers)

# 이게 정석풀이
# 좀만 더 생각하면

def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)
# 이렇게 도 풀이 가능

# 딕셔너리 쓸때 .item()이 일할 떄는 막상 자주 사용했지만 실제로 써보려고하면 잘 생각나지 않아서 알아둘겸 적었디.
