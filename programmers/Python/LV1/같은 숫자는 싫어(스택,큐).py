출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12906

스택으로 풀기:
def solution(arr):
  answer=[]
  for i in arr:
    if not answer or answer[-1] != i:
      answer.append(i)
  return answer

큐로 풀기:
from collections import deque

def solution(arr):
  answer=[]
  for j in arr:
    if not q or q[-1] != j:
      q.append(j)
  return list(q)
