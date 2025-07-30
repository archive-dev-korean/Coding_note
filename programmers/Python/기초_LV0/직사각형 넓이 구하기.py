# 문제 : 2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120860

# 정석적으로 구하면 이렇게 구하는게 맞다. 이번엔 생각하는게 좀 가로, 세로 길이 구하는 로직을 이렇게 구할 수 있다고 생각못했다.
def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    length_x= max(x) - min(x)
    length_y= max(y) - min(y)
    return length_x * length_y

# 조금더 쉽게 하면 이렇게 되는데
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

# 2차원 배열에서 max,min값은 각각 1차원 배열의 대소관계를 비교해서 반환함.
  
