--문제: 잡은 물고기의 평균 길이를 출력하는 SQL문을 작성해주세요. 평균 길이를 나타내는 컬럼 명은 AVERAGE_LENGTH로 해주세요. 평균 길이는 소수점 3째자리에서 반올림하며, 10cm 이하의 물고기들은 10cm 로 취급하여 평균 길이를 구해주세요.
--출처: https://school.programmers.co.kr/learn/courses/30/lessons/293259

--Null일 경우 10으로 변환(IFNULL사용), 소수점 2번째 자리까지 반올림해서 구함(Round사용)
select round(avg(IFNULL(LENGTH,10)), 2) as AVERAGE_LENGTH 
from FISH_INFO
