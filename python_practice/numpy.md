# 1. numpy(numerical python)

> numpy는 모듈로 vector와 matrix 계산 편리성 제공, ndarray(n-dimensional array) 자료구조 제공



0차원 => 하나의 숫자 => scalar e.g. 5

1차원 => 열로구성=>vector[1,3,5,7,9]

2차원=> 행과 열로 구성=>matrix([[1,2,3],[4,5,6]])

3차원 이상=>array라는 표현

### 1) ndarray

* 대부분 실수 float으로 이루어진다. 

* 같은 데이터 타입을 가져 원소의 데이터 타입을 모두 포괄 할 수 있도록 바뀐다.

  ```python
  b=np.array([1,2,3,4,14,'Hello'])
  print(b.dtype) #<U11 유니코드 형식
  ```

  

### 2) python list 와의 차이점

* ndarray는 모든 원소가 **같은 데이터 타입**을 가져야 한다.=>모든 원소가 같은 데이터 타입을 가지도록 스스로 맞춰준다.  list는 상관없다.
* 다차원이 존대한다. 

```python
a=[1,2,3,4]
#a=list()
print(a)#[1, 2, 3, 4]
b=np.array([1,2,3,4])
print(b)#[1 2 3 4]
print(type(b))#<class 'numpy.ndarray'>
print(b.dtype)#int32 32비트 짜리 정수
arr=arr.astype(np.int32) # data type 변경하는데 정수 될때 소수점 아래 다 버림
print(arr)

my_list=[[1,2,3],[4,5,6]]
print(my_list) # [[1, 2, 3], [4, 5, 6]]
my_array=np.array([[1,2,3],[4,5,6]], dtype=np.float64)
print(my_array) #[[1 2 3]
                 # [4 5 6]]
```



### 3) 생성하는 방법

  * zeros(스펠링주의),ones, empty, full,arange()스펠링 주의

  ```python
  #생성되는 데이터에 차이가 있다.
  
  arr1=np.zeros((3,4))
  print(arr1)
  [[0. 0. 0. 0.]
   [0. 0. 0. 0.]
   [0. 0. 0. 0.]]
  ```

  > ones

  ```python
  arr2=np.ones((3, 4),dtype=np.float64)
  print(arr2)
  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]
  ```

  > empty

  ```python
  arr=np.empty((3,4)) #초기화 하지 않아서 빠르게 공간만 설정
  print(arr)
  [[1.15161448e-311 3.06320700e-322 0.00000000e+000 0.00000000e+000]
   [1.15012172e-311 1.16095484e-028 5.28609931e-085 2.93625480e-062]
   [1.75300433e+243 4.90910702e-109 2.91237123e+257 4.71294503e+257]]
  ```

  > full

  ```python
  arr3=np.full((3,4),8,dtype= np.float64)
  print(arr3)
  [[8. 8. 8. 8.]
   [8. 8. 8. 8.]
   [8. 8. 8. 8.]]
  ```

  > arange(스펠링주의)

  ```python
  arr=range(0,10,2)
  print(arr)
  arr1=np.arange(0,10,1)
  print(arr1)
  print(arr1.reshape((2,5)))
  range(0, 10, 2)
  
  [0 1 2 3 4 5 6 7 8 9]
  [[0 1 2 3 4]
   [5 6 7 8 9]]
  ```

  * random으로 생성하는 방법

    * `matplotlib` 설치 필요
    * `np.random.normal`, `np.random.rand`, `np.random.randn` , `np.random.randint` ,  `np.random.random`

    ```python
    import matplotlib.pyplot as plt
    np.random.normal() # 정규분포에서 실수형태의 난수를 추출 
    #평균과 표준편차가 필요하다.
    my_mean=50
    my_std=2
    arr=np.random.normal(my_mean, my_std,(10000,))
    print(arr)
    plt.hist(arr,bins=100)
    plt.show()
    
    #np.random.rand(d0,d1,d2,d3...)#0이상 1미만의 실수를 난수로 추출, 균등분포로 난수를 추출
    arr=np.random.rand(10000)
    print(arr)
    plt.hist(arr,bins=100)
    plt.show
    
    #np.random.randn: 표준정규분포에서 실수형태로 난수 추출
    arr=np.random.randn(10000)
    print(arr)
    plt.hist(arr,bins=100)
    plt.show()
    
    #np.random.randint(low, high, shape): 균등분포로 정수 표본을 추출
    #np.random.randint(low, high, shape)
    arr=np.random.randint(10,100,(10000,))
    print(arr)
    plt.hist(arr, bins=10)
    plt.show
    
    #np.random.random(d0,d1,d2,d3): 0이상 1미만의 실수를 난수로 추출 균등분포로 추출
    arr=np.random.random((10000,))
    print(arr)
    plt.hist(arr,bins=100)
    plt.show
    
    ```
    
    ```
    
    ```


​    

### 4) 속성을 확인하는 방법

  > `ndim` : 차원의 수 표현, `shape`: 차원과 요소개수를 tuple로 표현

  튜플의 요소갯수=차원수 요소의 값이 차원의 요소 개수

  ```python
  #ndim
  # 1차원
  my_list = [1,2,3,4]
  arr = np.array(my_list)
  print(arr.ndim) => 1# 요소가 몇개있냐=차원의 수
  print(arr.shape) # 차원의 개수와 각 차원의 요소수 차원과 요소개수를 tuple로 표현 (4,)
  
  # 2차원
  my_list = [[1,2,3],[4,5,6]]
  arr = np.array(my_list)
  print(arr.ndim)  # 2
  print(arr.shape) # (2,3)
  
  # 3차원
  my_list = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
  arr = np.array(my_list)
  print(arr)# 3
  #[[[ 1  2  3]
  #  [ 4  5  6]]
  
   #[[ 7  8  9]
    #[10 11 12]]]
  (2, 2, 3)
  print(arr.ndim)  # 3
  print(arr.shape) # (2,2,3) 2면(depth), 2행, 3열
  
  #shape이 (2,2,3) 형태
  
  a=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
  ```

  ```python
  #shape
  #len=>python 몇개있니, 첫번째 차원의 요소갯수가 나온다. 행갯수
  #size: 모든 요소의 갯수
  
  my_list=[[1,2,3],[4,5,6]]
  arr=np.array(my_list,dtype=np.float64)
  print('shape : {}'.format(arr.shape))#(2,3)
  print('크기(len) : {}'.format(len(arr)))#2
  print('크기(size) : {}'.format(arr.size))#6
  
  my_list=[1,2,3,4]
  arr=np.array(my_list)
  print('shape : {}'.format(arr.shape))#(4,)
  print('크기(len) : {}'.format(len(arr)))#4
  print('크기(size) : {}'.format(arr.size))#4
    
# reshape(-1)
arr=np.arange(12)
arr1=arr.reshape(2,3,-1)#2면 3행 고정시키고 나머지는 알아서
print(arr1)
[[[ 0  1]
  [ 2  3]
  [ 4  5]]

 [[ 6  7]
  [ 8  9]
  [10 11]]]

arr2=np.arange(12)
arr2=arr2.reshape(2,-1)
print(arr2)
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]

  ```

### 5) `shape`변경 하는 법

* reshape 함수

```python
#direct access method-지양
my_list=[1,2,3,4]
arr=np.array(my_list, dtype=np.float64)
print(arr)
arr.shape=(2,2)#2행 2열 2차원으로 바꿔라
print(arr)

#reshape 함수 
arr=np.arange(12) #12개의 요소를 가지는 1차원 ndarray
print(arr)
[ 0  1  2  3  4  5  6  7  8  9 10 11]
arr1=arr.reshape(3,4) #3행 4열의 2차원 array 
arr1[0,2]=200
print(arr1)
print(arr)# reshape 함수는 새로운 ndarray 만들지 않고 view 생성
          # 원본이 그대로 변경된다. 

#원본손상 방지하기 위해서 `.copy()` 쓴다. 
arr=np.arange(15)
arr1=arr.reshape(3,5).copy()
print(arr1)
arr1[0,0]=100
print(arr1)
[[100   1   2   3   4]
 [  5   6   7   8   9]
 [ 10  11  12  13  14]]
print(arr)
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
```



* resize

> view 아니고 복사본 만들어서 바꿈

```python
#arr.resize
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
arr1=arr.resize(1,6) #원본을 바꿈, 결과 리턴 안함
print(arr1) #none이라고 나옴
print(arr)
[[1 2 3]
 [4 5 6]]
[[1 2 3 4 5 6]]

#np.resize(원본은 그대로 두고 복사본 만들어서 바/view아님)
arr=np.array([[1,2,3],[4,5,6]])
arr1=np.resize(arr,(1,6))
print(arr1)
[[1 2 3 4 5 6]]

arr1[0,1]=100
[[  1 100   3   4   5   6]]

print(arr)#변하지 않음
[[1 2 3]
 [4 5 6]]

arr.resize(3,4) #안맞는데도 변경할 수 있는데 다만, 0으로 채워짐
[[1 2 3 4]
 [5 6 0 0]
 [0 0 0 0]]
```





* ravel

> 가지고 있는 모든 요소를 포함하는 1차원의 ndarray로 변경, view 리턴

```python
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
arr1=arr.ravel()
print(arr1)

[[1 2 3]
 [4 5 6]]
[1 2 3 4 5 6]
```

# 2. indexing and slicing

> indexing(특정 위치의 데이터를 가져 오는 것)과 slicing(부분집합을 얻는 것) 

**slicing은 원본과 결과본의 형식이 같다.**

### 1)  enumerate

> 반복문 사용시 index를 추출 하기 위해서 사용

```python
arr=np.arange(20,10,1)
for idx,temp in enumerate(arr):
    print('인덱스 : {}, 값: {}'.format(idx,temp))
```



### 2) 일반적인 indexing

```python
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
print(arr)
print(arr[1,1])  # 6, 일반적인 2차원의 indexing
print(arr[1,:])  # [5,6,7,8]
print(arr[1:3,:]) # [[ 5  6  7  8]
                  #  [ 9 10 11 12]]
print(arr[0])     # [1 2 3 4] 
```



### 3) boolean indexing

> 조건을 가지고 원하는 요소만을 추출하고자 할때 사용하는 indexing 방법

* boolean mask: 원본 ndarray와 shape이 같고 그 요소값이 모두 boolean(true, false)로 구성된 ndarray

```python
#ndarray 중 짝수만 추출하고 싶다. 
np.random.seed(0)
arr=np.random.randint(1,20,(10,))
print(arr) # [13 16  1  4  4  8 10 19  5  7]
print(arr%2==0)
#boolean mask
#[False  True False  True  True  True  True False False False]
print(arr[arr%2==0]) # [16  4  4  8 10]

#ndarray안에 10보다 큰수가 몇개있는지 알아보려면?
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
print((arr>10)) #boolean mask 형태로 나온다. 
#[[False False False False]
#[False False False False]
#[False False  True  True]
#[ True  True  True  True]]

print((arr>10).sum()) #6
```



### 4) fancy indexing

> ndarray에 index 배열을 (list 형식)으로 전달하여 배달요소를 참조하는 방식

```python
arr=np.arange(0,12,1).reshape(3,4).copy()
print(arr)
print(arr[2,2]) #10
print(arr[1:2,2]) #[[6]]
#slicing은 원본과 결과본이 같다. 
#행을 먼저 slicing  1:2(exclusive)=>[[4 5 6 7]]뽑힌다. 여기서 2열 [6]
print(arr[1:2,1:2]) #[[5]]
print(arr[[0,2],2:3]) #[[2] 
#                     [10]]
# 일단 0행이랑 2행 뽑는다=>2열만 남긴다. 

# 하지만, print(arr[[0,2],[0,2]] 에러난다. 행 열에 둘다 fancy indexing 안된다. 
#np.ix_() 쓴다. 
print(arr[np.ix_([0,2],[0,2])])#[[0 2]
#                               [8 10]]
```

# 3. 연산

### 1) 사칙연산

* 사칙연산 기본적으로 shape 같아야 하나, broadcasting 가능 할 경우 연산 가능
* 곱셈은  앞쪽 행렬의 열과 뒤쪽 행렬의 행의 수가 일치
* 기본적으로 같은 위치에 있는 원소끼리 연산을 수행
* `broadcasting`: shape이 작은 쪽을 shape이 큰 쪽으로 맞추려는 시도. 변하면서 자동적으로 연산이 가능해지는 현상,한쪽으로만 맞춰야 한다. 배수인 경우에만 맞출수 있다. 

```python
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.arange(10,16,1).reshape(2,3).copy()
arr3=np.arange(10,16,1).reshape(3,2).copy()

print(arr1+arr2)
#[[11 13 15]
#[17 19 21]]

#행렬곱 연산은 함수를 이용 np.matmul()
print(np.matmul(arr1,arr3))
#[[ 76  82]
#[184 199]]

#broadcasting
print(arr1+10)
#[[11 12 13]
#[14 15 16]]
```

### 2) 비교연산

* 사칙연산과 유사하게  동작하고 같은 위치에 있는 것끼리 작도
* 각 matrix가 같은가를 알아보기 위해서 `np.arrat_equal()`

```python
np.random.seed(3)
arr1=np.random.randint(0,10,(2,3))
arr2=np.random.randint(0,10,(2,3))
print(arr1==arr2)
#boolean mask 나온다.
[[False False False]
 [False False False]]
print(arr1>arr2)

# 같니 물어보고 싶으면 함수 따로 np.array_equal(arr1,arr2)
print(np.array_equal(arr1,arr2))
```



# 4. iterator

> for 분보다 훨씬 짧은 시간이 걸린다. 데이터가 클 경우에

* 지시자, 포인터, 가리키는 거, numpy 배열에 있는 요소 가리켜서 사용할 수 있다.  인덱스 가지고 numpy array 사용할 수 있게 함
* 아래에 있는 화살표가 iterator라고 보면된다. 
* ![KakaoTalk_20210112_132142196](md-images/KakaoTalk_20210112_132142196.png)

```python
#1차원 ndarray의 요소를 출력하고 싶다.

#for문 사용할 때arr=np.array([1,2,3,4,5])
for tmp in arr:
    print(tmp,end=' ')

#iterator 사용할 때
arr=np.array([1,2,3,4,5])
it=np.nditer(arr, flags=['c_index'])
#iterator가 어떤 스타일로 움직이는지 flag로 말해줌1차원=> C언어의 index
while not it.finished: #iterator가 끝났니? 각각의 방 맨 끝까지 가서 종료되었니 true false로 말해준다. not false=true
    idx=it.index
    print(arr[idx],end=' ')
    it.iternext()
    
##2차원 matrix에 대해서 각 요소를 출력하고 싶어요
#면, 행, 렬에 대한 index가 각각 따로 있어야 되서 복잡해진다. 3차원은 for문 하나더,차원 하나씩 늘어날 때마다 for문 추가
arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape) #(2,3)

# for문을 사용할 때
for tmp1 in range(arr.shape[0]):# (2,3)=>2=> 행의 index
    for tmp2 in range(arr.shape[1]):#3=>열의 index
        print(arr[tmp1,tmp2], end=' ')

#iterator 사용할 때
it=np.nditer(arr,flags=['multi_index'])
#2차원 이상일떄는 다른 flag사용한다. 
while not it.finished:
    idx=it.multi_index #(0,0) fancy indexing 형태
    print(arr[idx], end=' ') #arr[1.2] 이렇게 들어온다. 
    it.iternext()
```



# 5. axis,집계함수, 수학함수,

### 1) axis

* numpy의 모든 집계함수는 axis를 기준으로 작동 
* axis를 설정하지 않으면 none으로 자동 설정, 대상의 범위가 전체로 지정
* 1차원에서 axix 는 0 밖에 없다. 
* 2차원에서  0 =>행방향, 1=>열방향
* 3차원에서 0=>면, 1=>행방향, 2=>열방향

```python
#1차원
arr=np.array([1,2,3,4,5])
print(arr.sum(axis=0))

#다차원
arr5=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr5.shape)
print(arr5.sum()) #전체 요소가 대상 #78
print(arr5.sum(axis=0)) # [22 26 30]
print(arr5.sum(axis=1)) #[ 6 15 24 33]
```

![KakaoTalk_20210112_150751105](md-images/KakaoTalk_20210112_150751105.png)



```python
np.random.seed(0)
arr=np.random.randint(0,12,(4,3))
#[[ 5  0  3]
#[11  3  7]
#[ 9  3  5]
#[ 2  4  7]]
print(arr.argmax(axis=0)) #[1 3 1]
print(arr.argmax(axis=1)) # [0 0 0 2]
```



### 2) 집계함수와 수학함수

* 집계함수: 합, 평균, 표준편차, 분산
* 수학함수: 최대, 최소, 제곱근, 제곱값, 로그값
* `np.argmax()`:최대값의 index가 리턴, `np.argmin()`: 최소값의 index 리턴
* `np.sqrt()`: 제곱근

```python
arr=np.arange(1,7,1).reshape(2,3).copy()
#[[1 2 3]
#[4 5 6]]

print(arr)
print(np.sum(arr)) #21
print(arr.sum())#21
print(np.mean(arr))#3.5
print(np.max(arr)) #6
print(np.min(arr)) #1
print(np.argmax(arr))# (2,3) 이런형식 아니다.=>5
print(np.argmin(arr))#0
print(np.sqrt(arr))
```

# 6. concatenation

* 차원 같아야 한다. axis 기준으로 연결
* `np.concatenate`((원래 array, 합칠거).`reshape`(2,3)),`axis`=0)

```python
arr=np.array([[1,2,3],[4,5,6]])
new_row=np.array([7,8,9])
result=np.concatenate((arr, new_row.reshape(1,3)), axis=0)
print(result)

#[[1 2 3]
#[4 5 6]
#[7 8 9]]

new_col=np.array([7,8,9,10])
result1=np.concatenate((arr,new_col.reshape(2,2)),axis=1)
print(result1)
#[[ 1  2  3  7  8]
#[ 4  5  6  9 10]]
```



# 7. 삭제

* axis 기준으로 삭제, axis 언급없으면 1차원 배열로 변환된 후 삭제

```python
arr=np.array([[1,2,3],[4,5,6]])
result=np.delete(arr,1)
print(result) #[1,3,4,5,6]
result=np.delete(arr,1,axis=0) #[1,2,3]
result=np.delete(arr,1,axis=1)
#[[1 3]
#[4 6]]
```



# 8. 기타

### 1) seed 

>  같은 난수가 추출되도록 설정

한번 실행한 후 다음 실행해도 똑같은 난수 생성되도록 설정

```python
np.random.seed(0)
arr=np.random.randint(0,100,(10,))
print(arr)
# 처음 실행하면 [28 36 90 44 48 59 74 54 91 21]
#두번째 실행하면 [56 39 29 32 48  9 33 60 88 55]
# 이렇게 안되게 방지한다. 

#이미 만들어진 난수의 순서 랜덤하게
np.random.shuffle(arr)
print(arr)
```

### 2) astype

> ndarray의 데이터 타입 변경 

```python
arr=np.array([1,2,2.3,3.5,4,1,5,7])
print(arr)#[1.2 2.3 3.5 4.1 5.7]
arr=arr.astype(np.int32)
print(arr)# [1 2 3 4 5]
```



### 3) 전치행렬(transposed matrix)

* `view`로써 원본을 바꾼다. 
* 수학적으로 표편할 때 위첨자로 대문자 T
* iterator for 문 사용하듯 반복해서 사용할 수 있다. 다차원 array 에 대해서 반복작업 수치미분을 iterator
* 행과 열을 바꾼것이다. 
* `arr.T` 요롷게 쓴다

```python
arr=np.a
[[1 4]
 [2 5]
 [3 6]]
```



### 4) 정렬

* np.sort: 인자로 들어가는 원본 ndarray에 변화 없고 복사본이 만들어짐
  arr.sort: 원본 배열에 변화. 리턴 없음

```python
arr=np.arange(10)
np.random.shuffle(arr) #[1 9 0 5 2 8 6 3 7 4]
print(np.sort(arr)) #[0 1 2 3 4 5 6 7 8 9]
print(np.sort(arr)[::-1]) #[9 8 7 6 5 4 3 2 1 0]
#sort 오름차순 정렬, [:]처음부터 끝까지 [::-1]역순으로 [::1]: 두칸씩 넘어가면서 슬라이싱
print(arr.sort()) #None
print(arr) #[0 1 2 3 4 5 6 7 8 9]
```

