# 문제 : 정수 배열 num_list와 정수 n이 매개변수로 주어집니다. num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.

# num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경합니다. 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.

# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120842

# 가장 정석적인 풀이는

def solution(num_list, n):
    # answer = [[]]
    return [num_list[(i*n):(i+1)*n] for i in range(len(num_list) // n)]

# 슬라이싱을 사용하는 방법인데 i가 0일 때는 num_list[0:n] 1일 때는 num_list[n:2*n]이렇게 된다 그러면 알아서 짤라짐

# numpy로도 구할 수 있는데
import numpy as np
def solution(num_list, n):
    reshaped = np.array(num_list).reshape(len(num_list)//n,n)
    return  reshaped.tolist()

# list로 변경해줘야 하는 번거로움이 있다.
# 어떤걸 쓰든 상관은 없을 것 같다.
