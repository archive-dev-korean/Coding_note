-- 문제 : USER_INFO 테이블과 ONLINE_SALE 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성해주세요. 결과는 년, 월, 성별을 기준으로 오름차순 정렬해주세요. 이때, 성별 정보가 없는 경우 결과에서 제외해주세요.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131532

SELECT YEAR(o.SALES_DATE) as YEAR, MONTH(o.SALES_DATE) as MONTH, u.GENDER, count(distinct u.USER_ID) as USERS
from USER_INFO u join ONLINE_SALE o on u.USER_ID = o.USER_ID
# where year(o.SALES_DATE) =2022 and month(o.SALES_DATE) in (1,2) and u.gender is not null
where u.gender is not null
group by year(o.SALES_DATE), month(o.SALES_DATE), u.GENDER
order by 1,2,3

-- where 절 조건을 처음에 잘못 줘서 틀렸다. 그리고 u.GENDER is not null 값을 줘야 하는데 count(distinct u.USER_ID) 떄문에 안줘도 되는거 아닌가?
-- 하는 의문이 들 수도 있지만
-- join 하는 과정에서 null 이 생성될 수도 있기 때문에 그 부분은 안 걸러진다.
-- 그리고 distinct 쓰는 이유는 한사람이 여러번 구매한 거 방지하기 위해 쓴다.
-- count(*)도 처음에 썼었는데 중복된 값이 모두 계산 돠어서 count(distinct 특정컬럼) 쓰는게 합리적인 것 같다. -> 이 부분 유의깊게 생각하자
