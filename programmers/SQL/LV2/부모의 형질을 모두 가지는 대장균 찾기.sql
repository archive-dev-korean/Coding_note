--문제 : 부모의 형질을 모두 보유한 대장균의 ID(ID), 대장균의 형질(GENOTYPE), 부모 대장균의 형질(PARENT_GENOTYPE)을 출력하는 SQL 문을 작성해주세요. 이때 결과는 ID에 대해 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/301647

--오답 1(비트 연산자 활용) :

# select ID, GENOTYPE, PARENT_ID as PARENT_GENOTYPE
# from ECOLI_DATA 
# where PARENT_ID is not null and GENOTYPE & 1 >0 and (GENOTYPE & 2 > 0 or GENOTYPE > 3)
# order by 1

-- 부모의 형질 데이터가 명시적으로 주어지지 않을 경우 다 안 구해 질 수 있음 결국 옳지 못한 쿼리

--오답 2(join활용) : 
# select d.ID, d.GENOTYPE, e.GENOTYPE as PARENT_GENOTYPE
# from ECOLI_DATA d join ECOLI_DATA e
# on
# d.PARENT_ID = e.ID
# where (d.GENOTYPE & e.GENOTYPE) = e.PARENT_ID
# order by 1

--원하는 결과가 나오지 않음 alias 를 조금더 명시적으로 표현해 주어야 할 것 같음

--정답 : 
SELECT C.ID, C.GENOTYPE, P.GENOTYPE PARENT_GENOTYPE
FROM ECOLI_DATA P JOIN ECOLI_DATA C
     ON P.ID = C.PARENT_ID
WHERE (P.GENOTYPE & C.GENOTYPE) = P.GENOTYPE
ORDER BY 1 

--명시적으로 누가 부모이고 누가 자식인지 구분해주니까 원하는 값 조회 가능
