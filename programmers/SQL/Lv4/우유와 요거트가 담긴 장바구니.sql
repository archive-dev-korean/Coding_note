-- 문제 : 데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다. 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/62284

-- 풀이(교집합 사용) : 
select distinct CART_ID
from CART_PRODUCTS 
      where cart_id in 
      (select CART_ID
      from CART_PRODUCTS
    where NAME = 'Milk'
      intersect
      select CART_ID
      from CART_PRODUCTS
      where NAME = 'Yogurt')
order by 1

-- 서브쿼리와 교집합을 이용해 원하는 값을 구할 수 있음 근데 문제는 mySQL은 Intersect를 지원하지 않는다는점??? 근데 내 코드는 돌아감
-- 심지어 정답임 성능은 데이터 양이 많으면 조금 안좋을 수 있지만 현재 데이터 에서는 문제가 되지 않을 정도라고함

SELECT CART_ID FROM CART_PRODUCTS 
GROUP BY CART_ID 
HAVING MAX(NAME = 'Milk') AND MAX(NAME = 'Yogurt')
-- 이런 코드도 있었는데 max(NAME=Milk) 나 max(NAME=Yogurt)는 값이 존재해야지만 1로 반환됨 없으면 0 그래서 having 절이 and구문으로 묶여 있기 때문에 둘다 결국 둘다 1이어야 group by 절이 돌아가고 결과가 반환됨
-- 이건 좀 천재인가? 같다. 
