# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/250121

풀이1(딕셔너리 사용):
def solution(data, ext, val_ext, sort_by):
    answer = []
    # 딕셔너리 사용
    ext_dict = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    target_idx = ext_dict[ext]
    for i in data:
        if i[target_idx] < val_ext:
            answer.append(i)
    answer.sort(key=lambda x:x[ext_dict[sort_by]])
    return answer

풀이2(문자열 비교):
   #딕셔너리 안쓰고 풀기
def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_idx =0
    sort_idx=0
    if ext =='code':
        ext_idx=0
    elif ext=='date':
        ext_idx=1
    elif ext== 'maximum':
        ext_idx=2 
    else:
        ext_idx=3
    
    if sort_by == 'code':
        sort_idx =0
    elif sort_by == 'date':
        sort_idx = 1
    elif sort_idx == 'maximum':
        sort_idx =2
    else:
        sort_idx =3
        
    for i in data:
        if i[ext_idx] < val_ext:
            answer.append(i)
    answer.sort(key=lambda x: x[sort_idx])
    return answer

그 외 오답 :
  # if ext =='code':
        #    if data[i][0] < val_ext:
        #     answer.append(data[i][0])
        #     # return answer
        # elif ext == 'date':
        #     if data[i][1] < val_ext:
        #         answer.append(data[i][1])
        #         # return answer
        # elif ext =='maximun':
        #     if data[i][2] < val_ext:
        #         answer.append(data[i][2])
        #         # return answer
        # elif ext=='remain':
        #     if data[i][3] < val_ext:
        #         answer.append(data[i][3]
        #       # return answer
    # return answer

근데 여기서 딕셔너리 써서 푸는게 좋을 것 같다 단순 만자열로 비교하면 틀리는 경우가 나온다
