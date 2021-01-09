# 1. numpy(numerical python)

> numpy는 모듈로 vector와 matrix 계산 편리성 제공, ndarray(n-dimensional array) 자료구조 제공



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
  ```

### 5) `shape`변경 하는 법

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

```



# 기타

