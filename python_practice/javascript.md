# 1. Javascript

> 브라우저 내 프로그램 실행과 관련된 부분

* 자바스크립트는 단독으로 사용되지 못하고 html 안에서 소환? 된다. 

* javascript 쉽게 작성하기 위해서 `jquery` 사용하는데 `jquery`는 잘 사용되지 않는 추세이다. pattern 사용하는 추세이기 때문. `jquery`는 호직을 내가 짜야해서 유지보수가 힘들다. head에 넣어준다.

  * `jquery`는 cdn 방식으로 import 의 개념이라고 생각

    ```javascript
     <script
                src="https://code.jquery.com/jquery-2.2.4.min.js"
                integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
                crossorigin="anonymous"></script>
        <script src="js/my_script.js">
        </script>
    ```
  
* 프린트/출력하는 법-`alert()`, `console.log('변수의 값: '+tmp1)` f10으로 확인
  
* 객체 만드는 법(python과 동일): dict와 똑같이 만든다. 
  
* 함수 만드는 법  `def add(x,y)` 파이썬과 같다. 
  
* 변수 선언하는 법 `let tmp1='sample;'` let으로 선언하고 ;로 끝마치기
  
  * 근데 `true` 파이썬이랑 다름
  
  ```java
  function openit(){
      alert('버튼 클릭됨')
          //프린트 기능을 하는 거-alert(), console.log()
          // alert는 좋은 기능이 아니다. 
      address='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
      input_id=$('#idid').val()
      input_date=$('#datedate').val()
      mymy_url= address + '?key='+input_id + '&targetDt=' + input_date
      location.href=mymy_url
}
  ```
  
* `jquery`사용법-`$(selector).method`

* selector란 HTML 엘리먼트를 지칭하는 특수 표기법

*  

  ```javascript
  1. 전체 선택자 : *
  $('*').css('color','red');
  
  2. 태그 선택자 : 태그명을 가지고 선택
  $('span').remove()
  $('li').css('background-color','yellow')
  
  3. 아이디 선택자 : ID속성을 이용해서 선택/아이디는 유니크하다. 
  $('#incheon').text('내일 아침에 초코스콘 먹을 생각이다. ')
  
  4. 클래스 선택자 : class속성을 이용해서 선택/아이디랑 비슷한데 중복가능
  $('.regionn').css('color','blue')
  
  5. 구조 선택자 : 부모, 자식, 형제 관계를 이용해서 선택
  //ol 자식으로 있는 li 찾아라
  $('ol>li').css('color','green')
  ```
  
  



# 2. HTML 

* 주석처리

```html
여러줄 주석처리
<!--이렇게 여러줄 주석처리한다. -->

//한줄 주석처리
```

* Head, body
  * head는 각종 설정 
  * 실제내용은 body
* 계층구조를 가진다.
* 태그: `<>`로 구성되는 `html `요소로 시작태그만있는 것도 있다. 
  * `<ol>`
  * `<ul>`
  * `<div>`
  * `<span>`
* `element`: HTML 구성요소
  * :`block level`: 요소가 한줄을 다 차지한다. 같이 쓸수 없어서 다음줄로 넘어간다. 
  * `inline element`:요소가 해당 내용만 차지한다. 



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script
            src="https://code.jquery.com/jquery-2.2.4.min.js"
            integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
            crossorigin="anonymous"></script>
    // 위 부분이 cdn 방식으로 query 입력할 수 있게 해주는 부분이다. 
    <script src="jj/openopen.js"></script>
    //html안에서 동적인 부분은 java로 가서 작성해줘야 한다. 하지만 javascript 단독으로는 안쓰임 약간 html에 embedded 
    //그리고 java가 어디있는지 head에서 알려줘야 한다.
</head>

<body>
일일 박스오피스 순위를 알아보아요

key : <input type="text" id="idid"> #id는 고유해야 한다.
<br><br>
date : <input type="text" id="datedate">

<input type="button" value="조회!!"
       onclick="openit()">


</body>
</html>
```



## 2. 