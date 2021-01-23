# Web programming

> HTTP protocol로 통신하는 클라이언트 프로그램/서버 프로그램을 개발
>
> Client/Server 구조로 되어 있다. 



## 0. internet

> network of network

인터넷 위에서 작동하는 여러 서비스, 웹서비스가 작동이 안되는 거다. HTTP, SNTP, FTP



## 1.  protocol

 데이터 통신에 대한 서로 지켜야할 약속, 데이터 주고 받는 약속

* stateless protocol
  * 서버(기차 예매 사이트)는 1개 client(예매하려고 하는 사람들)은 다수이다. 이때문에 연결을 계속 유지하면 서버측에 부담이 많이 된다. 따라서, request 받고 response를 주면 연결을 끊어버린다. 
  * 이때문에 client를 구분할 수 없다. 서로에 대한 정보가 없기 때문에 `session tracking` 을 한다. 
* HTTP protocol(hypertext transfer protocol): 웹서버와 클라이언트 프로그램이 데이터 주고받기 위해 사용하는 통신규약
  * TCP/IP protocol stack 위에서 동작하는 protocol로 ip 조소 기반으로 통신
  * text뿐만 아니라 이미지, 동영상 , pdf등을 전송하고 받을 수 있다. 여러 종류의 데이터를 주고 받을 수 있음

## 2. port

>  0~65536 안에 있는 숫자로 하나의 프로그램을(=프로세스) 지칭 

* 0~1024: reserved 
* 1025~65535: 사용자가 이용
* 메모장(3000), zoom(4000) 이런식으로 작동하는 프로그램마다 숫자
* web server는 일반적으로 80

## 3. IP주소

> network에 연결되어 있는 각종 기기에 부여되는 논리적 주소(바뀔수 있다는 의미)

*  in fact, 논리적주소인 ip 주소를 물리적 주소인 mac address(6자리)로 바꿔줘야 찾아갈 수 있다. 4자리임

* 근데 ip 주소 어려워서 domain name 쓴다. 

```python
HTTP://192.168.0.34:4000
(protocol) IP 주소   Port 
```

* web server와 web client는 request와 response를 주고 받는다. 



![img](md-images/2430783E56CEE04607)

## 4. web client

> web server에 접속하는 client 측 프로그램

* e.g. chrome. internet exploer, firefox, safari etc.
* 능동적으로 web server에게 정보를 요청
* web client application=>javascript, HTML,CSS
* 보통 우리가 작성하는 프로그램 
* Request 메시지 형태

```python
GET/book/romance(원하는 리소스 url) HTTP/1.1(사용하는 프로토콜 버전)
Host: www.example.com
    빈줄
body=> 또 다른 data 전달해야 하면 body 안에
```



* Request 요청방식(REST 방식)
  * Get: 리소스 가져오고, 얻어오고 싶은 경우 내가 전달할 data를 query string 형식으로 url 뒤에 붙여서 보낸다. e.g. 일일 박스 오피스
    * 장점: 사용하기 쉽다
    * 단점: url에 그대로 붙여서 사용해서 보안성이 없고 url에 길이 제한이 있기 떄문에 전달할 data에도 길이제한이 있다. 많은 양의 data 전달 못한다.  
  * Post: 새로운 데이터 서버쪽에 생성, 게시판에 글쓰기/ 전달할 데이터를 request 안 body에 담아 보낸다. 
    * 장점: 보안성이 있고 보내려는 데이터 길이제한 없음
  * Put: 서버 데이터 수정할때, 게시판 글 수정
  * Delete: 서버쪽 데이터 삭제
    * get, post 두가지로 crud 가능

## 5. web server

> web client의 요청을 받아 서비스를 제공하는 프로그램

* 보통 잘 작성하지 않고 많이 이용, 왜냐하면 다수의 client에게 서비스를 제공해야 해서 performance가 중요하고 세밀하고 잘 짜여야 하기 때문이다. 가져다가 쓰는 게 이득 e.g. apache 웹서버
* 서비스를 해주는 주체로 web client의 요청을 받아 서비스를 제공
* web server application=>django(python),servlet(java)
* e.g. IIS, internet information server, pracle web server
* 별도의 저장공간이 있는게 아니다. 담고 있는게 아니고 프로젝트 단위로 지각, 인지한다. 
* 정적 리소스에 대한 response만 가능하다. 
* web server program 실행=> web server가 프로젝트 인식하게 설정을 잡아야 client가 요청시 서비스를 제공할 수 있다.configure=> 인식한 프로젝트를 웹에서 전개(deploy)할 수 있고록 전개=>client브라우저 실행시 url 입력=> a.html 파일을 렌더링 

## 6. web application server(WAS)

![img](md-images/static-vs-dynamic.png)



* web server사 정적 리소스에 대한 response만 가능하기 때문에 web server는 프로그램 요청, 프로그램 처리를 web application server 에게 위임하고 request를 전달한다.

* WAS 안에 프로그램들 미리 만들어 주도 클라이언트가 요청할때마다 실행: django

* static web은 web server(정적인 response) 수준의 처리

  * HTML(내용)+CSS(표현)+Javascript(프로그램적 처리)

  * javascript: 마우스 클릭 입력 등 발생하는 다양한 이벤트를 javascript가 자동적 프로그램 처리를 해준다. 

    

* web server는 프로그램 수행 기능이 없음. 동적인 컨텐츠 만들어서 서비스 못함=> web server application 에게 위임. 서버쪽 별도의 웹 프로그램을 실행시켜 나온 결과 =>**server side web application**=>우리가 배울건 python framework django





![img](md-images/webserver-vs-was1.png)



## 7. round trip



![슬라이드1](md-images/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C1.PNG)



* 장점
  * Client 측 서버를 하나 마련하지 않아도 되서 돈 절약
* 단점
  * 효율적이지 못하고 데이터 전달량이 많다. 
  * WAS에 부하가 크다.

## 8. single page application

![슬라이드2](md-images/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C2.PNG)

* **client side web application**
  * front-end 개발과 관련이 있다. 
  * 브라우저 상에서 프로그램을 실행한다 . 화면에 보여주고, 넣어주고, 수행되는 내용을 client server를 호출해서 처리
  * 패턴으로 angular(google), react(facebook), vue js()
  * 브라우저 상에서 수행되는 내용
* **server side web application **
  * back-end 개발과 관련이 있다. 
  * 주로 패턴을 사용해서 개발한다. 패턴이 있으면 유지보수에 좋다. => front end 도 패턴쓰자. jquery 는 패턴이 아니기 떄문에 점차 안쓰는 추세
* client side web application 부하는?
  * cashing이라는 기법을 사용해서 부하줄임, client program 매번 로드 하지 않는다. => 처리해야 할 양적어진다. 
* WAS는 결과 데이터만 만든다.  e.g. csv, xml, json

* 장점
  * 효율적이다. client side web application과 server side web application 따로 구현할 수 있기 때문이다. 
  * WAS에 부하 적다. 네트워크에도 부하 적다. (네트워크 이용량이 돈이기 때문에 네트워크에 부하 줄이는 게 중요하다. )



## 기타

* library: 특정기능을 수행하는 코드 묶음 e.g. 함수, 클래스
* framework: library 포함하는 개념, 돌아가는 시스템 전체/기능을 구현한 코드 묶음/시스템 구조를 만든다/ 특정 기능을 하는 코드 단위 묶음/구축된 system 제공/많은 library 를 사용하고 이용한다. 
* library와 framework 차이: library는 하려고 하는 알고리즘과 로직이 없음. framework은 쇼핑몰이 돌아가는 코드에 대해서 알려준다.  e.g. jquery
* platform: 다른 프로그램을 실행시켜 줄 수 있는 환경이 되는 프로그램 e.g. os 계열, mac os, 리눅스