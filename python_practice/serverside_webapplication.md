# 1. web server

> 인터넷을 통해서 client의 request가 전달되었을 때 이 요청을 처맇는 일반적인 hardware와 software를 지칭

일반적으로 정적인 리소스(기존에 가지고 있는 리소스에 대한 서비스 제공)
* CGI(common Gateway Interface)
* 웹서버에서 프로그램(어플리케이션)을 수행시키기 위한 규칙/규약
  웹서버에서 동적인 기능 가능하게
  정적인 기능을 하는 web server에 동적 프로그램을 수행시킬 수 있는 기능을 부여 e.g. Pearl. C
  클라이언트가 웹서버에 요청하면 웹서버가 직접 프로그램 수행 e.g. apache NginX(경량화)
  문제점: 웹서버가 과부하됨, 정적, 동적 response둘다 해줘야 해서 많이 느려짐


# 2. WAS
> web server와 application server 분리 

* web server와 container로 되어 있음

![슬라이드2](md-images/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C2-1611836239503.PNG)



# 3. WSGI(Web Server Gateway Interface)

> 파이썬에 종속된 개념, 파이썬 스크립트(웹어플리케이션)이 웹서버와 통신하기 위한 규약

![case1case2 case3](md-images/case1case2%20case3.png)




# 3. Django

> python으로 만들어진 web application framework

웹서버와 통신하기 위해서는 WSGI 규약 지켜야 하는데, framework을 사용할줄 알면 이 규약을 지켜 web application 작성할 수 있다. 

## 1) MVT pattern 사용

> 전체 프로그램 구조와 관련된 패턴

* 특정기능은 이렇게 하면 좋다더라 와 같은 경험을 논리적으로 구현

* 패턴을 사용하지 않으면 유지보수 문제가 발생

* e.g. singleton pattern, observer pattern, MVC pattern
* 획일적인 적용 어려워서 다양한 변형있다. e.g. MVM, MCC..

코드가 섞여 들어가지 않게 분리해서 유지보수한다. 

**Model**: 데이터 및 데이터 베이스, data handling 관련 부분으로 데이터 베이스 관련된 사람이 유지보수

**View**: user interface 관련된 부분으로 UI 디자이너가 주로 수행

**Contol**: business logic 주로 개발자가 수행 

request오면 control이 model 한테 데이터 요청, model은 작동해서 데이터 결과만 controller 한테 전달, view가 UI 만들어서 HTML로 만들어서 controller 한테 줌, contoller는 client에게 response 전달

![case1case2 case37](md-images/case1case2%20case37.png)

**M(Model)**: MVC와 동일하게 데이터와 관련된 핸들링

**V(View):** controller의 역할을 함 로직처리한다. 

**T(Template):** view의 역할을 한다. 



## 2) ORM (Object Relational Mapping)방식

> 데이터 베이스를 활용하는 특수한 방식으로 객체 관계 mapping을 활용

* Database 관련된 이야기
* 계층형 DB=> Network DB=> Relation DB
  * 계층형: top down 구조, 사람이 사고하는 것과 유사하며, data 유지, 보수 , 관리가 쉬우나, 데이터 간의 연동이 힘들다. 폴더구조와 유사
  * network:  graph 구조, 하지만 구현이 힘듬
  * Relation: excel 같은 테이블 형태, 정형 데이터 처리하기위해서는 data type 맞춰야 하고 정형화되어 있어야 함, table에 맞는 column 형태,,, 비정형 DB는 따로
    * e.g. IBM, Oracle, MS
  * 객체지향: 구현이 힘들고 relation DB가 지나치게 좋음
  * 객체-관계 지향 DB: Django!!
* 단점: 속도, 사용성 문제
* 장점: 편하게 제어, 객체 db 제어 가능 python class의 객체 사용해서 제어하겠다. 내부적으로 자동으로 sql 생성되서 db 사용됨 원래는 sql 알아야 한다. query 날려야 함

![case1case2 case388](md-images/case1case2%20case388.png)

## 3) 관리자 페이지 자동생성

## 4) elegant URL

* URL  디자인이 직관적이고 쉽다. 



# 5) 기타

front end(html+css+javascript)=>webstorm

backend=>pycharm



 