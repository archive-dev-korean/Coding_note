# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/340213
def solution(video_len, pos, op_start, op_end, commands):
    # mm = int(input()) // 60
    # ss = int(input()) % 60
    def to_sec(mmss: str):
        m, s = map(int, mmss.split(":"))
        return m*60 + s
    def to_mmss(sec: int):
        m = sec //60 
        s = sec % 60
        return f"{m:02}:{s:02}"
    
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    # commands=[]
    if op_start <= pos <= op_end:
        pos=op_end
    for i in commands:
        if i == 'prev':
            # pos -= 10
            # if op_start <= pos <= op_end:
            #     pos = op_end
            # elif pos < 10:
            #     pos = 0
            # else:
            #     pos
            pos = max(0, pos - 10)
        else:
            # pos += 10
            # if op_start <= pos <= op_end:
            #     pos = op_end
            # elif pos > video_len:
            #     pos = video_len
            # else:
            #     pos
            pos = min(video_len, pos+10)
        if op_start <= pos <= op_end:
            pos = op_end
    return to_mmss(pos)

# 원래 메인 로직은 for 문 안에 주석 처리한 부분이다 그러나 정답 처리에서 한가지 경우에 대해 오답이 나서 다시 최대 최소값으로 수정함.
# 시간 계산 로직도 참고함
