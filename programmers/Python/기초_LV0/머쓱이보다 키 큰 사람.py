문제 : 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

def solution(array, height):
    answer = 0
    array.sort()
    for i in range(len(array)):
        if array[i] > height:
            return len(array) - i
        else:
            return 0

# 너무 어렵게 풀었다. 특히 retrin len(array) -i 이 부분 

# 쉽게 풀면
def solution(array, height):
    answer=0
    for i in array:
        if i > height:
            answer +=1
    return answer

# 이렇게
