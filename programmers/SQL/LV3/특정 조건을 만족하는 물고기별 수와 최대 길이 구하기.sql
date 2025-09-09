--문제 : FISH_INFO에서 평균 길이가 33cm 이상인 물고기들을 종류별로 분류하여 잡은 수, 최대 길이, 물고기의 종류를 출력하는 SQL문을 작성해주세요. 결과는 물고기 종류에 대해 오름차순으로 정렬해주시고, 10cm이하의 물고기들은 10cm로 취급하여 평균 길이를 구해주세요. 컬럼명은 물고기의 종류 'FISH_TYPE', 잡은 수 'FISH_COUNT', 최대 길이 'MAX_LENGTH'로 해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/298519

--정답1( 60%의 정답률) :  
select count(*) as FISH_COUNT,
max(LENGTH) as MAX_LENGTH,
FISH_TYPE
from FISH_INFO 
where ifnull(LENGTH, '10')
group by 3
having avg(LENGTH) >= 33
order by 3

--where 절에서 null 처리가 들어가서 결과는 똑같이 나올 것이라고 생각함 하지만 틀린 경우도 있기에

select count(*) as FISH_COUNT,
max(LENGTH) as MAX_LENGTH,
FISH_TYPE
from FISH_INFO 
group by 3
having avg(ifnull(LENGTH, '10')) >= 33
order by 3

-- 이렇게 쓰는것이 명확하고 모든 경우의 수에 들어맞음
