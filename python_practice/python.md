# 1. data type


|       ()        |  []  |       {}       |
| :-------------: | :--: | :------------: |
| tuple(생략가능) | list | dictionary,set |



### 1) numeric

> int, float, complex

### 2) sequence

> list,tuple,range

* range와 list의 차이점은 list는 실제 데이터가 들어 있다는 것이고 range는 의미가 들어 있다는 점이다. range는 적은 양의 메모르 필요하다. 
* range는 for문과 자주 사용된다. 



```python
#list comprehension
# 리스트를 생성핳때 반복문과 조건문을 이용해서 생성
a= [1,2,3,4,5,6,7]
#또 다른 리스트 만들고 싶다. 
list1=[tmp*2 for tmp in a]
list2=[tmp*2 for tmp in a if tmp % 2==0]
print(list1)
print(list2)

#range(시작, 끝, 증가치)
a=range(10) #range(0,10)이런형식으로 print된다. 
print(7 in b) # in은 true와 false가 나오는 논리 연산자이다. 
print(a[0])#1나온다. 인덱싱과 슬라이싱이 가능하다.
print(a[0:])
print(a[-1])
```







### 3) tuple

* 리스트와 유사하나 **소괄호로 생성(())**
* 수정하거나 삭제할 수 없다. 고정해 놓고 수정하거나 변경 하면 안되는 값
* 요소가 하나면 반드시 뒤에 ,
* 튜플은 리스트와 사용법 같다. 

```python
var1=tuple((1,))
print(var1)
(1,)
```



### 4) text sequence

> str 결국하나의 리스트이다.

```python
#파이썬은 ''와 ""를 구분하지 않는다. 같은 데이터 타입이 아니면 에러가 난다. 
a=100
b='개'
print(str(a)+b)

a='this is a sample test'
print(a)
print(a[3]) #s

print('sam' not in a) # false not in 연산자도 있으며 결과는 논리값

# len, upper, lower, count
a=cocacola
len(a) #8 글자 길이 알고 싶을때 사용
print(a.count('c')) #3 내가 원하는 문자가 총 몇번 나오는가
print(a.upper())
print(a.lower())

# 문자열 출력관련 formating
apple_count=3
orange_count=10
a='나는 사과를 {}개 오렌지는 {}개 가지고 있어요!!'.format(apple_count, orange_count)



```



### 4) mapping

> dict(dictionary)

* 중괄호를 감싸서 표현하고 ({}) **키-값** 형태로 데이터를 저장한다. 키값에 접근할 때 []와 key값을 활용하여 접근한다.
* {key: value}: json 
* 키 값으로 다양한 값이 들어올 수 있다. 
* 반복해야하는 횟수 알면 for 문 사용하고 특정 조건 충족할때까지 반복해야 하는 거면 while 사용한다.
* 들여쓰기로 block 표현하지 않고 indent 사용한다. (4번 space) 

```python
var1=dict({"key1":"value1","key2":"value2"})
var2={"key1":"value1","key2":"vakue2"}
print(var2.get("key3"))#원래 그냥 프린트 하면 error 나는데 get으로 가져오면 error 안난다. 
----------------------------------------------------------#
##dict에 새로운 내용추가
var={}
print(var)
var["key1"]=10
var["key2"]=20
var["key3"]=30
var["key1"]=40 #dictionary 는 키의 중복을 허용하지 않아서 이미 생성된 키에 한 값의 추가가 아닌 수정이 일어난다. 
print(var) 
{'key1': 40, 'key2': 20, 'key3': 30}

var.setdefault('key1',20)##setdefault 쓰면 고정된다 다음에 key1으로 추가해도 안변함

a['adress']='서울' # 키 값 존재하지 않으면 data 추가
#program의 유연성 측면에서는 장점이나. 논리 오류에 취약함, 무결성 안정성 
a['adrass']='서울'
#adress 바꾸고 싶었는데 추가되었다는 거야

#--------------------------------------------------------#
#key, value 값만 출력
print(var.keys())#key 값만 프린트
dict_keys(['key1', 'key2', 'key3'])

print(var.values())#value 값만 프린트
dict_values(['value1', 'value2', 'value3'])

print(var.items()) # items는 리스트처럼 만들어준다.하지만 정확하게 리스트 아니어서 슬라이싱이나 인덱싱 불가능하다. 하지만 반복문 가능(이터레이터) list로 바꾸면 리스트 처럼 사용가능 
dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

print('key3' in var)#key 유무 검사
True
print('key4' in var)
False
#삭제하기-------------------------------------------------------
del a['age']

a.clear() #a안에 있는 값 다지움
```



### 5) set

> 중복을 배제하고 순서가 없는 자료구조  출력할때 그냥 오름차순 정렬되지만 인덱싱이 안된다. 인덱싱은 순서가 있다는 뜻이다. 
> {}를 이용한다.--dict 대신 key 가 존재하지 않고 value 만 존재한다. 

```python
a={1,2,3,1,2,3} #{1,2,3}

# 집합연산
result=a&b #교집합
print(result)

result=a|b#합집합, union
print(result)

result=a-b#차집합, difference
print(result)#{1,2,3}

# 데이터 추가 및 삭제
#set에 데이터 추가, 삭제
#a={} #빈 딕셔너리로 인식된다
a=set() #차라리 이렇게 해라, append는 맨끝에 붙여라, 순서 존재 안해서 add
a.add(7) #한개 추가하고 싶을때
a.update([1,2,3,4]) #여러개 추가하고 싶을 때 update
a.remove(4)
print(a)
#del은 있다는 것만 알아두고 안쓰는게 좋다. 요소 삭제하고 싶을때는 함수 이용해서 지워라 remove같은
```



### 6) bool 

> 논리타입으로 true 혹은 false 형태

* and, or, not 사용할 수 있음
* and는 두개 다 true여야 true

```python
##python 에서 다음의 경우는 false
'''
1) 빈 문다열('') 논리 타입으로 표현하면 false
2) 빈 리스트([]) false로 간주
3) 빈 tuple (()) false
4) 빈 dict({})
5) 숫자 0은 false로 간주되고 숫자는 true
6) None 아무것도 없어 존재하지 않아. 값이 없다. 
공백은 문자열인데 내용이 없는 문자열 none은 아예 값이 없다
```



# 2. 연산자 

### 1) 사칙연산자

* **: 거듭제곱
* //: 나누기 연산후 정수부분만
* %: 나누기 연산후 나머지만

### 2) 비교연산자

* 참/거짓 반환
* == : 같다.
* != : 양측값이 다른가요

### 3) 논리연산자

* and, or, not
* and: 하나라도 false이면 false로 출력
* or: 하나라도 true면 true
* not: 반대로, true이면 false, false면 true 반환 0은 없다. 0이외는 있다라고 규정

```python
print(True and True)
True

print(1>2 and 2>1)
False
```

### 4) 할당연산자

| 할당연산자 |                             기능                             |           예            |
| :--------: | :----------------------------------------------------------: | :---------------------: |
|     =      |                 왼쪽 변수에 오른쪽 값을 할당                 |  a=b;a에 b를 할당한다.  |
|     +=     | 왼쪽 변수에 오른쪽 변수 값을 더하고 그 결과를 왼쪽 변수에 할당 |      a +=b; a=a+b       |
|     -=     |   왼쪽 변수에 오른쪽 값을 빼고 그 결과를 왼쪽 변수에 할당    |       a=-b; a=a-b       |
|     *=     |  왼쪽 변수에 오른쪽 값을 곱하고 그 결과를 왼쪽 변수에 할당   |      a *=b는  a=ab      |
|     /=     |  왼쪽 변수에 오른쪽 값을 나눈 후 그 결과를 왼쪽 변수에 할당  |      a/=b는 a=a/b       |
|     %=     | 왼쪽 변수에 오른쪽 값을 나눈 후 그 나머지를 왼쪽 변수에 할당 |      a%=b는 a=a%b       |
|    //=     |   왼쪽 변수에 오른쪽 값을 나눈 후 그 몫을 왼쪽 변수에 할당   | a//=b는 a=a//b를 의미함 |
|    **=     |  왼쪽 변수에 오른쪽 값 제곱하고 그 결과를 왼쪽 변수에 할당   | a**=b는 a=a**b를 의미함 |



# 3. 조건

### 1) If

```python
condition_t=True

condition_f=False

condition_t=True
condition_f=False

if condition_t: #if에서는 indent 안하고 if 다음에 실핼딜 코드를 tab으로 분리한다. 
    print('hello')
    print('world')
if condition_f:
    print('HELLO')
    print('WORLD')

print('last')
hello
world
last
```

### 2) if~else 조건분기

* 포함여부에 대한 내용 써줄때  `in`을 써준다.  

```bash
a=20
if a%3==0:
    print('3의 배수에요!!')
elif a%5==0:
    print('5의 배수에요!!')
elif a%7 ==0:
    print('7의 배수에요!!')
elif a%11==0:
    pass ##그냥 넘어가게 설정 할 수도있다. 
else:
    print('조건에 해당되는게 없어요')
```



# 4. 반복

### 1) while

* `%f` 실수,  `%d` 정수, `%s` 문자

```bash
while 조건:
	실행코드 1
	실행코드 2


count=0
while count < 5:
        print('%d 번째' %(count))
        count += 1
0 번째
1 번째
2 번째
3 번째
4 번째
```

### 2) for

* 범위가 정해져 있다
* while보다 조건 탈출에 대한 부담감을 줄일 수 있다. 

```bash
#for i in range, list, tuple(sequence data type)
for tmp in [1,2,3,4,5]:
        print(tmp) 
        #print는 default로 형태로 사용하면 출력후 줄바꿈
		#만약 가로로 쓰게 하고 싶으면 end 속성을 이용

for tmp in [1,2,3,4,5]:
        print(tmp,end='')

        
for tmp in [1,2,3,4,5]:
        print(tmp,end=' ')
```



# 5. 함수

> 객체지향,  특정 기능을 수행하는 코드의 묶음

* 가독성을 높이기 위해서 함수명은 소문자, 밑줄을 이용해서 만든다.  e.g. student_name
* 내장함수와 사용자 정의 함수가 있다. 

### 1) 사용자 정의함수

```python
def division(x): # x가 인자이다. 기본적으로 인자 갯수를 맞워줘야 한다. 
    if x%2:
        return True
    else:
        return False
    print('running') #return이 실행되면 그 이후에 있는 코드 실행하지 않음

def my_sum(a, b, c):
    result = a + b + c
    return result #값 반환하고 종료
#사용자 정의 함수 뒤에 2줄

def f(x,y=20):##y=20이 부분이 기본값 이러면 인자갯수 부족해도 에러 안남
    print('running '+ str(x)+ ' ' + str(y))
    return True

#인자의 갯수가 가변적인 경우
def my_sum(*tmp):
    result=0 # 함수 안의 영역이랑 밖의 영역 구분되서 누적 작업의 기초마련
    for t in tmp:
        result += t
    return result

print(my_sum(5,7,8))


# 여러개의 값을 리턴하는 함수, 사실 여러개의 값아니고 tuple
def multi_return(a,b):
    result1=a+b
    result2=a*b
    return result1, result2#사실 튜플이다. ()생략됨

multi_return(10,20)
```



### 2) 인자(parameter)

> call-by-value: 넘겨준 인자값이 변경되지 않는 경우->immutable(불변의)  복사해서 사용하는개념 원본 수정 안함
> call-by-reference: 넘겨준 인자값이 변경되는 경우->mutable #list

```python
def my_func(tmp_value, tmp_list):
    tmp_value = tmp_value + 100
    tmp_list.append(100)
    
data_x = 10
data_list = [10,20]

my_func(data_x,data_list)

print('data_x : {}'.format(data_x))   # 10   => immutable (숫자, 문자열, tuple)
print('data_list : {}'.format(data_list)) # [10,20,100]   => mutable (list,dict)

# local variable과 global variable

tmp = 100#여기있는게 global variable

def my_func(my_tmp,x):
#     global tmp #밖에 있는 tmp 가져다가 쓸께
    my_tmp = my_tmp + x #안쪽 tmp와 바깥쪽 tmp 다른 것으로 간주,  
    return my_tmp
#함수는 함수 내부에서 사용하는 공간 따로 있다.
print(my_func(tmp,20))

# 이렇게 global keyword로 global variable을 함수내에서 사용할 수 있음
# 하지만 별로.. why-> 독립적인 모듈인 함수가 외부에 영향을 받음
# 따라서, 프로그램 수정하기 어렵다.
# cntrl / 주석 잡기 혹은 풀기
```

### 3) 내장함수

* 엄청 많고 다다익선

  ```python
  # 1. all(x)
  # 반복가능한 자료형 x에 대해서 모든 값이 True이면 True. 만약
  # 하나라도 False이면 False처리를 해주는 함수
  
  a = [3.14, 0, 'Hello', True] #0빼면 true 된다.
  print(all(a))
  
  # 2. any(x)
  #반복가능한 자료형 x에 대해서 하나라도 True이면 True. 만약
  #모든데이터가 False이면 False처리를 해주는 함수
  a = [0, 1, '', None]
  print(any(a))
  
  #3. len(x)
  # x의 길이를 알려주는 함수
  
  # 4. 자료형 바꿔주는 함수
  #int(), float(), list(), tuple(), dict(), str(), set()
  ```

  





# 6. 프로그래밍 유형

### 1) 절차적 프로그래밍

> 프로그램을 기능으로 세분화 시키고 각각의 기능을 함수로 모듈로 만든다.  e.g. C++

* 은행 프로그램 구현하기 위해서->은행이 가지고 있는 기능 파악(예금.외환, 대출, 보험)->예금 업무를 대상으로 다시 기능을 세분화->예금(자행,타행, 무통장, 출금)
  결국은 더 이상 세분화 할 수 없는 기능들이 도출되고 이런 단위기능들을 함수로 구현
* 장점: 프로그램을 쉽고 빠르게, 프로그램 설계가 오래 걸리지 않음 
  프로그램 설계를 누가 하던 거의 동일한 설계, 생산성 높일 수 있음
* 단점: 프로그램의 규모가 커지면 복잡해지게 된다. 다른 곳에도 영향을 미치게 된다. 
  유지보수가 힘들다. 얽히고 섞여있다.개발 비용보다 유지보수 비용이 더 커진다.  기존 코드 재사용에 한계(함수단위로 가져다 쓰던지, 코드를 복붙해서 재사용)
* 학계나 상대적으로 간단한, 특별히 유지보수가 필요없는 이런 프로그램들은 절차적 프로그램 방식으로 구현!
* 인터넷의 보급, 유지보수 수요 급증, 서비스업 발달은 특히 유지보수 필요



### 2) 객체지향

> 해결하고자 하는 문제를 그대로 프로그램으로 묘사하려고 한다. 

* 객체지향 프로그램(OOP): 주어 동사가 있다고 생각해라. 묶어서 쓰는 것으로 재사용할 수 있어서 묶어두고 재사용해서 효율성을 높인다. 붕어빵틀이라고 생각 변수와 함수의 집합체를 이용하여 미리 정의된 변수와 함수를 사용할 수 있는 공간, 변수를 만들때  해당 변수에 미리 정의된 변수와 함수를 사용할 수 있도록 하는 것 , 클래스로 할당할 값을 객체(instance)라고 부름, 객체는 스스로 속성을 가지며 특정행위 할 수 있는 주체
*  현실세계의 개체를 프로그램적으로 모델링하는게 중요
  * 해결해야하는 문제를 그대로 프로그램으로 묘사=> 프로그램을 구성하는 주체를 파악 은행을 구성하는하고 있는 주체들 => 은행, 계좌, 사람, 지점=> 이 주체들이 어떻게 서로 상호작용하는지를 프로그램적으로 묘사.
  * 자동차가 가지는 속성 : 도어수, CC, 현재 속도, 차 가격, 차의 색상,                     CC, 현재속도 => 변수 => 속성, 필드, property, attribute
    자동차가 가지는 행위 : 전진한다, 후진한다, 깜빡이를 킨다, 와이퍼를 움직인다,기어를 변경한다 => 함수 => method
* 장점: 프로그램의 유지보수성과 재사용성에 이점
* 단점: 설계와 구현이 어렵다. 사람마다 정의하는 문제가 달라서 어렵다. 
* 서비스류 프로그램들은 유지보수성 때문에 객체지향적으로 구현
* python언어에서는 class안의 변수를 property(속성,프로퍼티) class안의 함수를 method(메소드)



# 7. 클라스(class)

>  현실세계의 개체를 프로그램적으로 묘사하기 위해서 사용하는 설명서 같은 개념, 프로그램적으로 표현하는 개념. 속성과 매소드의 집합, 데이터가 담겨져 있지 않음

* (현실세계의)객체를 (프로그램적으로)모델링의 (프로그래밍)수단
  추상 데이터 타입(새로운 데이터 타입을 만들어내는 수단)

* 사용자 정의 `class ` 만들때 반드시 첫글자는 대문자. 

* class variable: 모든 instance가 공유하고 있는 것이며 인자로 `self`를 쓰지 않음 가능한 instance variable을 쓰는 것이 좋다. 

  ```python
  class Student(object):
       scholarship_rate= 3.0 #class variable
      def __init__(self, name, dept):
          self.name=name
          self.dept=dept
      
      def get_student_info(self):
          return '이름은 : {}, 학과는 : {}에요!'.format(self.name, self.dept)
  stu1=Student('홍길동','철학')
  stu2=Student('신사임당','컴퓨터')
  print()
  ```

  

* class variable과 class method 모두 동적으로  추가해서 사용가능하나. 비추천.  method 를 통해서 property 이용하고 제어해라

  ``` python
  Student.scholarship_rate=3.5 #객체가 아닌 class 명 써줘
  stu1.scholarshiprate=3.5 #stu2 에서는 그대로 속성하나 더 생성한거야 class variable 수정한게 아니라
  ```

  

* `magic function`

  > 직접 호출 안하고 특정상황이 되면 자동 호출
  
  * `__init__` : 인스턴스 만들어지는 시점에 자동으로 만들어짐, 인스턴스에 초기화 작업 속성 만들어주고 속성 초기화
	  `__str__`: print 같이 instance를 문자열로 변환시키면 자동호출
	  
	
	`__del__`: instance가 메모리에서 삭제될때 자동호출, 객체가 삭제될 때 이 객체가 사용한 resource를 해제 시켜줘야 한다. 특히 database나 네트워크 사용하면 연동된 처리 끝마치고 지워줘야 한다. 
	  `__lt__`: <에 의해서 호출 less than
	
	  `__gt__`: > 에 의해서 호출 greater than
	
	  ```python
	  class Student(object):
	      def __init__(self, name, dept,grade):
	          print('객체 생성했다.!')
	          self.name=name
	          self.dept=dept
	          self.grade=grade
	          
	      def __del__(self):
	          print('객체 reference 다 지움!!')
	          
	      def __gt__(self,other): #other는 뒤에 있는 객체
	          if self.grade > other.grade:
	              return True
	          else:
	              return False
	      
	      def __str__(self):
	          return '이름은 : {}, 학과는 : {}'.format(self.name, self.dept)
	      
	      def get_student_info(self):
	          return '이름은 : {}, 학과는 : {}에요!'.format(self.name, self.dept)
	      
	  stu1=Student('홍길동','철학',2.2)
	  stu2=Student('신사임당','컴퓨터',4.5)
	  print(stu1 > stu2)#원래라면 error=> gt method 써주면 작동
	  print(stu1)#원래라면 메모리 주소만 print str method 써주면 
	  #이름은 : 홍길동, 학과는 : 철학
	  # 두번째 실행부터 del method 계속나온다. 처음에 할당된 메모리 영역에서 두번째 실행하면 또 메모리 영역 할당하고 그 전에 가지고 있던 메모리 reference 지우기 때문이다. 
	  ```
	
	  

### 1) 객체(instance)
class를 기반으로 프로그램에서 사용할 수 있는 메모리 영역을 할당할 , 데이터 담겨져 있음

* **self** : instance의 메모리 주소를 가지고있는 reference variable

* 각각의 instance는 다른 메모리 공간, 각 시작주소가 다르다. self가 같아보이지만 다르다. e.g. 객체 3개면 각각 name, dept 다르다.

  * class가지고 instance만들면 특정 메모리 공간 할당 return은 시작주소 리턴받아서 사용하는 거다.

* instance variable:  instance에 각각 할당되는 변수 instance 각각이 따로 가지고 있음

  ```python
  class Student(object):#superclass namespace
      def __init__(self, name, dept):#class namespace
          self.name=name#instance variable
          self.dept=dept#instance variable
      
      def get_student_info(self):#instance method
          return '이름은 : {}, 학과는 : {}에요!'.format(self.name, self.dept)
  #instance
  #stu1은 메모리 주소값 reference variable이다. 
  stu1=Student('홍길동','철학') #0x1234 이렇게 객체마다 메모리 장소 다른데 이를 지칭하는게 self
  stu2=Student('신사임당','컴퓨터')#0x5678
  ```

* 본래 객체지향은 객체가 가지고 있는 속성과 매소드만 사용할 수 있음 

* 현재 stu1 instance는 2개의 property, 1개의 method 가지고 있음

* `dot operator`  객체가 가지는 속성에 access 할때 사용 `.`앞에 `class` 뒤에 property, method
* 메모리 주소는 계속 변경, 같은 라인이라도  다시 실행하면 다른 메모리 주소 또 할당, 이전 객체를 사용할 수 있는 끈 reference가 떨어지고 자동으로 삭제처리된다. 



```python
stu1.name='최지수'
stu1.names='최지윤'
```



* **namespace**: 객체들의 요소들을 나누어서 관리하는 메모리 공간
  e.g. instance namespace
  e.g. class namespace
  
  * name 이름은 같지만 관리되는 space는 달라서 동일한게 아니다
  * 우리가 속성이나 method 이용할 때 계층구조를 이용해서(namespace를 따라가면서, 속성과 method를 찾는다)
  * instance namespace=> class namespace=>superclass namespace (이 방향으로 사용하려는 속성이나 method를 찾아)
  
  ```python
  class Student(object):
      
      scholarship_rate=3.0 #
      
      def __init__(self, name, dept,grade):
          self.name=name
          self.dept=dept
          self.grade=grade
      
      def get_student_info(self):
          return '이름은 : {}, 학과는 : {}에요!'.format(self.name, self.dept)
  
      def is_scholarship(self):
          if self. grade >=self.scholarship_rate:#원래는 Student.scholarship_rate 객체부분에서 없으면 class로 찾으러 간다. 
              return True
          else:
              return False
          
      
  stu1=Student('홍길동','철학',2.0)
  stu2=Student('신사임당','컴퓨터',4.0)
  
  print(stu1.is_scholarship())
  ```
  
  

### 2) 매소드(method)

`class` 안에서는 함수라고 안하고 `method`라고 한다. 


* ()가 있으면 method라고 볼수 있음

* 속성을 direct 하게 접근하는 방법이 있으나 logical 오류를 배제 할 수 없다. e.g. stu1.grade=-1

* instance가 가지고 있는 속성은 외부에서 직접적인 변경이 불가능 하도록 코드 작성

* method를 통해서 코드 변경하도록 작성


  * public과 private

    > public: 어디에서나 속성과 함수를 사용할 수 있는 경우를 지칭 속성과 함수를 자유롭게 access 할 수 있는 case

    ```python
    class Student(object):
        scholarship_rate= 3.0 
        def __init__(self, name, dept, grade):
            self.name=name 
            self.__dept=dept #public=>private(direct acess 안됨. method 통해서만)
            #class 외부에서 호출하는 거는 먹히지 않음
            self.grade=grade
    ```

    

* method 통해서 property 이용과 제어

* instance method

  * 인스턴스 메소드는 self를 인자로 받아서 instance variable을 생성, 변경, 참조하기 위해서 사용

 ```python
  class Student(object):
      def __init__(self, name, dept):
          self.name=name
          self.dept=dept
      
      def get_student_info(self):
          return '이름은 : {}, 학과는 : {}에요!'.format(self.name, self.dept)
  stu1=Student('홍길동','철학')
  stu2=Student('신사임당','컴퓨터')
  print(stu1.name)
  print(stu2.name)
  print(stu1.get_student_info)# <bound method Student.get_student_info of <__main__.Student object at 0x00000160A8234DC8>>
  #함수이름이 메모리 주소를 가지고 있고 ()이 호출기능을 해서 에러가 났다. 
 ```

* class method

  * `@classmethod`class method를 이용하여 인스턴스가 공유하는 class variable를 변경, 수정, 참조한다. cls를 인자(class를 지칭)로 받는다.

	```python
	@classmethod
      def change_scholarship_rate(cls, rate)
          cls.scholarship_rate=rate
  ```
  
  

* static method

  > self나 cls를 인자로 받지 않음,일반적인 함수가 class 내부에 존재

  ```python
      @staticmethod
      def print_hello():
          print('Hello')
  ```

  

* 동적으로 method 추가 가능하지만 지양

  ```python
  def my_func(a,b):
      return a+b
  stu1.my_func=my_func
  stu1.my_func(1,2)
  ```


### 3) 상속(inheritance)

> 상위 클라스의 특징을 이어 받아서, 확장된 하위 클라스를 만들어 내는 방법

* 목적:  한번 정의한 class를 필요에 따라 재활용하고, 코드의 반복을 줄이고 compact한 코드를 작성하기 위해
* 장점: 코드의 반복을 줄이고 재활용성을 높일 수 있다. 클래스 재활용하려면 독립적인 class인 경우 더 좋아
* 상위 클래스가 하위클래스가 서로 긴밀하게 연결(tightly coupled) 뭉텅이로 데리고 다녀야 한다. 
* 부모와 자식같은 관계,,,어떤 `class`던  적어도 object class 상속 계층관계로 class상속받으면서 내려온다, python의 모든 class는 상속관계
* 객체지향의 꽃,  재사용성을 확보, 기존의 class를 확장해서 사용할 수 있음
* 상속 양날의 검=> not always
* 상속 사용하면 class간의 계층구조, 관계가 생기게 됨
* 상위 클래스(super class,upper class, parent class,부모 클래스): 상속을 내려주는 class e.g. object
* 하위class(sub class,child class):상속을 받아서 확장하는 class e.g.Student

```python
class Unit(object):
    def __init__(self, damage, life):
        self.utype= self. __class__.__name__#오브젝트 클라스가 가지고 있는 거#클라스 이름에 대한 정보
        self.damage=damage
        self.life=life
        
my_unit=Unit(100,200)
print(my_unit.damage)
print(my_unit.utype)

#하위 class(sub, child class)
class Marine(Unit): #제대로 하려면 중복되는 코드지워
    def __init__(self, damage,life,offense_upgrade):
        super(Marine, self).__init__(damage, life)#상위 클라스를 찾아가라 Unit이 가지고 있는 init()
        self.offense_upgrade=offense_upgrade
        
#marine이 독자적으로 가지고 있는 것만 작성

marine_1=Marine(100,200)
print(marine_1.damage)
print(marine_1.utype)
print(marine_1.offense_upgrade)
```



```python
class Student(object):#object 상속 상속받고 있는 class 명시
   
    #~~~~~#
    def__init__(self,name, dept, num, grade):#속성을 init 안에서 명시
    #시작인자는 반드시 self, 객체 파생되었을 때 어떤 데이터 어떻게 셋팅 할지 알려준다.
        self.name=name
        self.dept=dept
        self.num=num
        self.grade=grade
        #전자의 self 는 class가 가지는 속성을 의미 후자의 self는 인자로 들어오는 변수
    #~~~~~#method이다. 
    
    #~~~~method~~~#
     def get_stu_info(self):
        return '이름 : {}, 학과 : {}'.format(self.name,self.dept)
    #self .name 아니면 error 난다. 왜냐하면 속성은 클라스 내부에서 선언된 변수이기 때문에
        
stu1 = Student('강감찬','경영학과','20201120',3.4)
print(stu1.get_stu_info())
#~~~method~~~#

#~~~instance~~~~#
students=[]
students.append(Student('홍길동','철학','20200111',1.5)) #객체생성
students.append(Student('김길동','영어영문','20200113',3.5)) #객체생성
students.append(Student('신사임당','컴퓨터','20200115',4.5)) #객체생성

print(students[1])
```



```python
my_list=list() #list class의 인스턴스 생성
print(type(my_list)) #instance가 어떤 class로부터 파생되었는지 알려줌
```



```python
#Student라는 붕어빵틀을 만들거야 그 속성으로 이름, 국어, 영어, 수학점수있는다, 이 class에 최지수라는 instance추가(붕어빵) 찍어낼거야
class Student(object):
    def __init__(self, name, kor, eng, math):
        self.name= name
        self.korean= kor
        self.english= eng
        self.math= math
#기능
#say_hello 함수
#평균average 함수

def say_hello(self):
        return '안녕하세요 {}님'.format(self.name)
def average(self):
        return(self.korean+self.english+self.math)/3
    
stu1=Student('최지수',100,100,99) #instance 만들기
print(stu1.math) #dot operator 생각해라.
```

```python

```



# 8. 기타

### 1) lambda 표현식

`lambda`: 한줄로 함수를 정의하는 방법

* 함수처럼 사용되지만 함수 아님 함수의 이름이 없기 떄문에 anonymous function), 람다식(lamda expression)이라고 부름

* 함수를 간편하게 작성할 수 있어서 다른 함수의 인수로 넣을 때 주로사용함

* 변수= `lambda` 입력변수 1, 입력변수 2, ...: 대체표현식

  ```python
  def my_sum(a,b,c):# 별도의 scope 공간을 갖고 처리된 결과를 돌려줘야 한다. 처리된 결과 호출한 곳으로 보내려면 return 있어야 된다.
      return a+b+c
  #my_sum(10,7,8)#
  
  f=lambda a,b,c: a+b+c  # 리턴 키워드가 없다. 처리된 결과를 돌려주는 게 아니다. 표현 바꿔줄뿐 독자적인 처리 공간이 아니다. 
  print(f(1,2,3))#람다가 하는 일 print(f(10.20,30))->print(10+20+30)
  ```

  



### 2)  모듈(module)

> 함수나 변수 혹은 클래스 모아 놓은 파일

* 확장자가 .py로 끝나는 python소스코드는 무조건 모듈
우리는 주피터 노트북 사용하고 있고 확장자.ipynb 이기 때문에 모듈아님

* 파일 나눠서 만든다. 다른 파일에 있는 함수, class 가져와, 다른 파일에 있는 내용을 객체화.
* 다른 파이썬 파일을 불러와서 우리 코드에서 이용할 수 있도록 해주는 기능
* import : 모듈을 불러들이는 키워드, 파일을 객체화 시켜서 우리코드가 사용하는 메모리에 로드
* module을 import 하면 객체화되서 들어오게 된다. file 명만 쓰면된다

```python
import modulse as m1# 너무 길어서 이렇게 자주 쓴다
from (모듈) import (무언가) #모듈안에 있는 무언가 
from module1 import my_pi
import network.my_sub_folder.my_network_module #상위폴더부터 쭉써야 한다 폴더 안에 깊숙이 들어가 있으면. 
#print(network.my_sub_folder.my_network_module.variable1)# 그래서 as m1 이렇게 해준다. 
from network.my_sub_folder import my_network_module
# import * from 모듈명시
```

### 3) 예외처리

* 문법적인 오류 아닌데 오류

* runtime 오류 떄문에 중간에 강제종료 되는데 이때 계속 진행 할 수 있도록 해주는 기능

* database, network 이용할 때, 내 프로그램은 문제 없는데, 예기치 못한 문제, 데이터베이스 꺼져있거나 외부적인 요인으로 인해서 에러가 날때 외부리소스 사용할 때 문제 예방 

* `try` `except` `else` `finally`

```python
def my_func(list_data):
    my_sum=0
    #exception이 발생할 수 있는 여지가 있는 코드에 대해서 try
    try: #세번째 값이 없어서 runtime 오류 날것이다. 
        my_sum-list_data[0]+list_data[1]+list_data[2]
    except Exception as err:# Exception: 모든 종류의 오류 지칭
        print('실행시 문제가 발생했어요!!')
        my_sum=0 
    else:# error 발생안하고 else 있으면 수행
        print('실행시 문제가 없어요~')
    finally:#오류여부와 상관없이 무조건 실행
        print('만약 finally가 존재하면 오류여부에 상관없이 실행되요')
        
    return my_sum

my_list=[1,2]
print(my_func(my_list))
```

### 4) 파일처리

* 주로 `pandas`에서 수행하지만, 기본적인 파일처리

```python
my_file=open('mpg.txt','r') #용도 명시-읽을거야? 쓸거야?

while True:#몇 줄인지 모르니까 range 안쓰고 while 쓴다. 
    line=my_file.readline()
    print(line)
    if not line:
        break  #while문 탈출
my_file.close()# 리소스 해제 처리해줘야 한다. 
```

