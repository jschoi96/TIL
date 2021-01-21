# Web programming

> HTTP protocol로 통신하는 클라이언트 프로그램/서버 프로그램을 개발
>
> Client/Server 구조오 되어 있다. 

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

## 6. web application server(WAS)

![img](md-images/static-vs-dynamic.png)



* web server사 정적 리소스에 대한 response만 가능하기 때문에 web server는 프로그램 요청, 프로그램 처리를 web application ser





![img](md-images/webserver-vs-was1.png)







## 기타

* * 

    