# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    # 키패드 좌표 설정
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    left_pos = pos['*']
    right_pos = pos['#']
    answer = ''
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left_pos = pos[num]
        elif num in [3,6,9]:
            answer += 'R'
            right_pos = pos[num]
        else:
            # 거리 계산 (맨해튼 거리)
            lx, ly = left_pos
            rx, ry = right_pos
            nx, ny = pos[num]
            
            left_dist = abs(lx - nx) + abs(ly - ny)
            right_dist = abs(rx - nx) + abs(ry - ny)
            
            if left_dist < right_dist:
                answer += 'L'
                left_pos = pos[num]
            elif right_dist < left_dist:
                answer += 'R'
                right_pos = pos[num]
            else:
                # 거리 같으면 hand 기준
                if hand == "left":
                    answer += 'L'
                    left_pos = pos[num]
                else:
                    answer += 'R'
                    right_pos = pos[num]
    return answer


# 좌표값으로 푸는 거 라고 생각은 했었는데 거리 계산이랑 이런 것 때문에 틀렸을 것 같다. 가까운 거리 구해서 가운데 키패드를 눌러야 하니 좀 이 로직 때문에 틀렸을 것이다 아마 혼자 구해도
