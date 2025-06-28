--문제 : PRODUCT 테이블에서 만원 단위의 가격대 별로 상품 개수를 출력하는 SQL 문을 작성해주세요. 이때 컬럼명은 각각 컬럼명은 PRICE_GROUP, PRODUCTS로 지정해주시고 가격대 정보는 각 구간의 최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000)으로 표시해주세요. 결과는 가격대를 기준으로 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131530

--복잡한 풀이 : 
# SELECT case
# when price between 0 and 10000 then 0
# when price between 10001 and 20000 then 10000
# when price between 20001 and 30000 then 20000
# when price between 30001 and 40000 then 30000
# else 40000
# end as PRICE_GROUP,
# count(*) as PRODUCTS
# from PRODUCT 
# group by 1
# order by 1 asc

--이런식으로 상품 가격을 case로 지정해서 구할수 있긴함 -> price의 범위가 안주어져 있어서 어디까지 해야 할 지 잘 모름


--간단한 풀이 :
select truncate(price, -4) as price_group, count(*) as products
from product
group by 1
order by 1 asc

--truncate 함수 써서 간단히 구할 수 있음.
