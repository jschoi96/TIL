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
  //공백은 후손, +는 형제를 지칭(바로 다음에 나오는 형제)
  $('ol li').css('color','green')
  $('ol + span').css('color','blue')
  
  6. 속성선택자 []해서 찾아준다.
  $('input[type=button]').disable() //disable 안먹힘
  
  7. 혼합해서 사용되는 경우
  console.log($('ul > .myList').text())// 태그선택자=>class 선택
  
  8. 순서선택자: eq 중간에 있는 것 까지 뽑을 수 있음
  console.log($('ol > li:eq(1)').text())
  
  9.기타
  console.log($('ol > li:last').text())
  //ol 안에 있는 li중에서 제일 마지막의 text가져와라
  console.log($('ol > li:first+li').text())
  //ol 안에 있는 li 중에서 2번째거
  
  ```




* `text()`: 태그 사이에 있는 텍스트 가져올때

  ```javascript
  console.log($('#apple').text())
  console.log($('#apple').text('꼭꼭 씹어서 먹으니까 배불러서 기분이가 좋다'))
  //text()안을 채우면 해당 텍스트로 바꾸라는 의미이다. 
  ```

  

* 속성값을 알아내고 바꾸고 싶을때-`attr()`

```javascript
console.log($('input[type=text]').attr('size',50))
 $('input[type=button]:first').removeAttr('disabled')
```



* 이름이 없는 함수, 묵시적 함수=>`lambda`함수 처럼 사용

```javascript
//명시적 함수
function my_func(){
    
}
//묵시적 함수
$('ol > li').each(function(idx,item){
    console.log(idx+'번째'+$(item).text())
//묵시적 함수는 변수에 담아서 쓴다. 함수를 독립적으로 선언하지 못하고 변수 같은 곳에 저장해서 사용, 함수를 하나의 값으로 사용=>first class/함수가 하나의 값으로 사용되기 때문에 함수를 다른 함수의 인자로 사용가능
```

* 제거하는 법
```javascript
  $('div.myStyle').empty()//자기자신은 삭제하지 말고 후손 모두 삭제
  $('div.myStyle').remove()//자기자긴 포함 다 삭제
```

* element 추가하는 법

```javascript

let my_div =$('<div></div>>').text('mae muller')
let my_img =$('<img />').attr('src','img/images.jpg')//img는 끝나는 태그 없어서 주의

//붙이는 방법//

1. append() : 자식으로 붙이고 맨 마지막 자식
2. prepend() : 자식으로 붙이고 맨 처음 자식
3. after() : 형제로 붙이고 바로 다음 형제
4. before() : 형제로 붙이고 바로 이전 형제
$('ul').append(my_li)
$('ul').prepend(my_li)
$('ul > li:eq(1)').after(my_li)
$('ul > li:last').before(my_li)
```



* `ajax`
  * 	댓글쓰는 거
  * 	  query string은 url 아님 ajax는 화면 refresh 되지 않음


  ```javascript
  let my_url= open_api +'?key=' +user_key +'&targetDt=' + user_date
  location.href=my_url
  //화면 refersh 되서 원하는 바가 이루어지지 않음
  ```

  

  ```javascript
  $.ajax({
        url :open_api,
        type : 'GET',
        dataType : 'json',
        data : {
            key : user_key,
            targerDt : user_date,

        },
        success : function() {
            alert('서버성공')
        },
        error : function() {
            alert('뭔가이상함')
        }
    })
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
  * `<ol>`:ordered list 로 숫자로 리스트로 만들어줌
  * `<ul>`: unordered list로 bullet으로 리스트 만들어줌
  * `<div>`: 눈에 보이는 기능은 없으나 내용을 한개 단위로 묶기 위해서 사용, 스타일 주기도 편함, block level
  * `<span>`: div와 유사하나 inline element
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

* 사용자 입력양식
  * 서버에 데이터 전송, 로그인 프로세스와 같이 사용자의 입력을 받아 서버를 호출한다. 
  
  * `<form action="서버쪽 프로그램 " method="post 같이 어떤 호출방식">`
  
  * 일방적으로 `form`태그를 사용, 체크리스트, 입력상자, 버튼 등 형태 다양 
  
    ```javascript
    <form action="#" method="post">
                <input type="text" id="uId" size="20">
                    //한줄 짜리 입력상자. size는 입력 상자 크기, 20글자 정도 들어온다.
    ```
  
    

# 3. CSS

* 원칙은 파일 따로관리 한다. CSS, javascript, html

```javascript
//$('div').css('color','red')
    //$('div').css('background-color','yellow')
//함수로 만들수 있지만 css 호출될때마다 화면 렌더링을 다시한다. 비효율적임





//head 부분에 class로 만들어 놓고 원하는 부분에 
 <style>
        .myStyle{
            width : 400px;
            height : 900px;
            background-color: aliceblue;}
    </style>

<div class="myStyle"> //원하는 부분 구역정해서 style 줄 수 있다. 
        <ul>
            <li>최지수</li>
            <li>최지윤</li>
        </ul>
    </div>

$('div').addClass('myStyle')// 함수로 실행할때 클라스 지정해 주는 법도 있다. 
```

