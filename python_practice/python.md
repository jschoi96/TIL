# 1. basic concepts

### 1) dictionary

* 중괄호를 감싸서 표현하고 ({}) **키-값** 형태로 데이터를 저장한다. 키값에 접근할 때 []와 key값을 활용하여 접근한다.

```python
var1=dict({"key1":"value1","key2":"value2"})
var2={"key1":"value1","key2":"vakue2"}
print(var1)
print(var2)
print(var1["key1"])
print(var2["key2"])
print(var2.get("key3"))#원래 그냥 프린트 하면 error 나는데 get으로 가져오면 error 안난다. 

{'key1': 'value1', 'key2': 'value2'}
{'key1': 'value1', 'key2': 'vakue2'}
value1
vakue2
None
#----------------------------------------------------------#
var={}
print(var)
var["key1"]=10
var["key2"]=20
var["key3"]=30
var["key1"]=40#dictionary 는 키의 중복을 허용하지 않아서 이미 생성된 키에 한 값의 추가가 아닌 수정이 일어난다. 
print(var) 
{'key1': 40, 'key2': 20, 'key3': 30}

var.setdefault('key1',10)
Out[45]: 10

var.setdefault('key1',20)##setdefault 쓰면 고정된다 다음에 key1으로 추가해도
Out[46]: 10

var.setdefault('key2',30)
Out[47]: 30

print(var)
{'key2': 30, 'key1': 10}
#----------------------------------------------------------#
var={'key1':'value1','key2':'value2','key3':'value3'}

print(var)
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

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
```

### 2) tuple

* 리스트와 유사하나 **소괄호로 생성(())**
* 수정하거나 삭제할 수 없다. 고정해 놓고 수정하거나 변경 하면 안되는 값
* 요소가 하나면 반드시 뒤에 ,
* 튜플은 리스트와 사용법 같다. 

```python
var1=tuple((1,))
print(var1)
(1,)
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
condition1 = True
condition2 = True
condition3 = True

if condition1:
    print('첫 번째 조건')
elif condition2:
    print('두 번째 조건')
elif condition3:
    print('세 번째 조건')

else:
    print('네 번째 조건')
첫 번째 조건
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
for 변수 in range(0,10):
	실행코드1
for 변수 in (리스트 or 문자열 or 딕셔너리 or 튜플):
	실행코드1
```



