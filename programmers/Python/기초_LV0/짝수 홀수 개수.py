# 문제 : 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(num_list):
    answer = []
    for i in range(len(num_list)):
                   if num_list[i] % 2 ==0:
                        answer.append([i])
                   else:
                        # answer.append([j])
                    return answer

 # 처음에 이렇게 정석적으로 생각하다가 좀 이상하게 풀려서

def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        if i%2 ==0:
            even +=1
        else:
            odd +=1
    return[even,odd]
# 변수 두개 지정해서 따로 구하는게 좋을 것 같다는 생각이 들어서 이렇게 하게 되었다. 리스트로 반환 하라는 조건이 있기때문에
# 마지막에 []로 묶어주면 된다.
