***암기사항***
- 비트 연산자 (효율적인 수 처리, 집합 표현, 상태 압축 등에서 사용)
  > &(and) 둘다 일이면 일
  > 
  >|(OR) 하나라도 1이면 1
  > 
  >^(XOR) 다를 떄 1
  > 
  > ~(NOT) 비트 반전(보수)
  > 
  >  `<<`(왼쪽 쉬프트 2의 곱)
  > 
  >  `>>`(오른쪾 쉬프트 2의 나눗셈)
  >
  > ex) select 6&3;  ---- 110 & 011 = 010 ->2
  > 
  > ex) select 6|3;  ---- 110 | 011 = 111 ->7

- DATE에서 연,월,일 추출
  > MYSQL 기준 YEAR(날짜), MONTH(날짜), DAY(날짜)
  > 
  > orcale 기준 EXTRACT(YEAR FROM 날짜), EXTRACT(MONTH FROM 날짜), EXTRACT(DAY FROM 날짜) 이렇게 적거나
  > 
  > TO_CHAR(날짜, 'YYYY') 이런 식으로 적음 TO_CHAR(날짜, MM) TO_CHAR(날짜, DD) 
