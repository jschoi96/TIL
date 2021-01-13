# 1.  data 표현 방식

## 1) CSV(comma seperated values)



* **장점** : 많은 데이터를 표현하기에 적합, 데이터 사이즈를 작게할 수 있음
* **단점** : 데이터의 구성을 알기 어려움 구조적 데이터 표현이 힘듬
         사용이 힘들고, 데이터처리를 위해서 따로 프로그램을 만들어야 함
         데이터가 변경됬을때 프로그램도 같이 변경 => 유지보수문제가 발생
* 데이터의 크기가 무지막지하고 데이터의 형태가 잘 변하지 않는 경우는
  CSV형태가 가장 알맞은 형태
* 예)홍길동,20,서울,김길동,30,인천,최길동,50,제주,신사임당,40,광주,...

## 2) XML(eXtended Markup Language) 

* 1990년 초반, 중반

* 장점 : 데이터의 구성을 알기 쉬움 사용하기 편함
         프로그램적 유지보수가 쉬움

* 단점 : 부가적인 데이터가 많음

* <person><name>홍길동</name><age>20</age><address>서울</address></person>
     <person><name>김길동</name><age>30</age><address>인천</address></person>
     <person><name>최길동</name><age>50</age><address>제주</address></person>

  

  

## 3) JSON(JavaScript Object Notation)

* 현재 일반적인 데이터 표현방식
  자바스크립트 객체표현방식을 이용해서 데이터를 표현하는 방식
* JSON은 데이터 표현방식이지 특정 프로그래밍 언어와는 상관이 없다.
* **장점** : 데이터의 구성을 알기 쉬워요. 사용하기 편함
         프로그램적 유지보수가 쉬워요!, XML보다 용량이 작음
* **단점 **: CSV에 비해서는 부가적인 데이터가 많음
*  { name : '홍길동', age : 20, address : '서울' }

txt도 많이 쓰이지 않나요?  => 파일의 종류
확장자를 이용해서 표현 => .txt, .jpg, .mpg, .exe
txt도 csv일종인가요?   => .csv
                       => .json  .xml



