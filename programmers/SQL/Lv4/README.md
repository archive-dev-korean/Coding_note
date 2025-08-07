# 계층쿼리 
- MySQL인 경우 : 재귀 CTE -> with recursive 테이블명 as 이런 형태로 사용함. 루트노드와 자식노드를 직접 지정해 줘야함. 부모 자식간 연결도 join을 사용해 직접 연결 해 줘야함.
  - 루트 노드 지정할 경우 where 루트값 is null 이런 방식으로 지정
  - 일반적으로 for문 처럼 사용할 수도 있음.
    - with recursive example as (
      - select ... --> 초기값
      - union all
      - select ... --> 재귀적으로 실행될 부분
      - from example
      - where ...)
      - select * from example;
  - 이렇게 쓰면 for문처럼 재귀적으로 실행될 부분이 초기값에서 반복적으로 실행됨.
  - % 주의사항 % : UNION ALL을 사용해야 재귀가 계속됨(UNION은 중복 제거 때문에 멈출 수 있음)
  - 재귀 깊이 제한 있음 : 설정 가능
  - 종료 조건을 where 절에서 잘 잡아야 무한 루프 방지 가능
      
- oracle일 경우 : connect by 로 사용해서 루트 노드를 start with로 지정해서 간단하게 사용가능.
