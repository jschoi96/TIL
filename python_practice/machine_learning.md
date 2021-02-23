# AI

## 1. AI

> 인간이 가지는 특유의 학습능력, 추론능력을 컴퓨터로 구현하려는 가장 포괄적인 개념, 그 중 한가지가 machine learning

* data mining: data 간의 상관관계, data feature , 특징들간의 상관관계를 밝히거나 새로운 속성들 알아냄
* AI 는 explicit program(rule based programming)으로 해결할 수 없는 것들을 해결하기 위해 등장 
* 규칙이 너무 많거나, 경우의 수가, 조건이 너무 많은 경우=> machine learning 

## 2. machine learning

> AI를 구현하기 위한 하나의 방법으로 data 이용해서 data pattern을 학습하게 한다. data 특성과 pattern 학습해서 미지의 data에 대한 추정치를 계산

### 1) regression

> regression model :어떠한 데이터에 대해서  그 값에 영향을 주는 조건을 고려하여 데이터의 평균을 구하기 위한 함수
>
> 어떤 연속형 데이터 y와 이 y의 원인이라 생각되는 x간의 관계를 추정하기 위해서 만든 y=f(x)+e(error)
* 기본적으로 classical linear regression model 가정함

*  어떠한 데이터에 대해서 그 값에 영향을 주는 조건을 고려하여 그 데이터를 가장 잘 표현하는 함수 

* 평균은 대표성을 나타낸다. 

* 독립변수가 1개인 함수를 가정하면 y= b0(기타 영향을 주는 요인)+b1(x에 영향을 주는 영향)x

* 주어진 데이터를 가장 잘 표현하는 직선 찾는다. 

* regression toward mean

* 단변량 선형회귀(종속변수의 갯수-1개)

* y=h(x1,x2,,,xk;b1,b2,b3,,,bk)+e

  h는 조건에 따른 평균을 구하는 함수(회귀모델)

  모델은 단숭화하기 위해서, 우리가 해결해야 하는 현실은 복잡하기 떄문이다. 

  오차항의 평균이 0, 정규분포

  독립변수와 종속변수가 선형

  데이터에 아웃라이어가 없어야 

  독립변수와 오차항은 독립

![단순회귀분석 이미지 검색결과](data:image/jpeg;base64,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)

* simple linear regression, multiple linear regression
* ![image-20210222170703140](md-images/formula2.png)

* 머신러닝에서는 `y=wx+b` weight 는 가중치 b는 bias
  * data가장 잘 표현하는 w와 b를 찾아가는 과정
  * error 값을 제곱해서 loss function 찾는다. 평균제곱오차가 최소가 되는 weight와 bias



* loss function(cost function, 비용함수)

  ![회귀 모델에 대한 성능 평가 지표들](data:image/png;base64,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)				

  * training dataset의 정답(t)와 입력 x에 대한 계산값 y(모델의 예측값)의 차이를 모두 더해 수식으로 나타낸 식

  * 최소제곱법: 손실 함수를 만드는 과정

  * loss function 과 MSE(Mean squared error)

  * 최소제곱법을 이용해서 loss function을 만들고  만든 loss function이 최소가 되게 하는 w와 b를 학습과정을 통해

  * MSE와 loss function은 같은가?

    * 항상 같지 않다. MSE만 가지고 loss function 만들어낼수 없음

    * simple linear regression에서만 같다. 

      

* 경사하강법(gradient descent algorithm)

* <img src="https://miro.medium.com/max/2284/1*jNyE54fTVOH1203IwYeNEg.png" alt="Gradient Descent Algorithm and Its Variants | by Imad Dabbura | Towards  Data Science" style="zoom:50%;" />

  * loss function은 w에 대한 이차함수이다. 
  * loss function 이 최소가 되는 w를 찾기 위해 사용된다.
  * 처음에는 랜덤으로 한점 찍었다가



### 2) SVM(support vector machine)

### 3) decision tree

### 4) random forest

### 5) naive bayes

### 6) KNN

### 7) Neural Network 

> deep learning: 신경망을 이용해서 학습하는 구조화된 알고리즘이 최근 개선 및 개발됨 (CNN, RNN, LSTM,GAN)

* 예측이 정확한 추론값을 도출하나 computing 시간이 오래 걸림

### 8) clustering(k-means, DBSCAN)

### 9) reinforcement learning



# 3.  분류

> data를 어떻게 학습하는 가에 따라서 나눌 수 있다. 
>
> 입력값을 x(feature), 정답t(label)

### 1)  지도학습(supervised learning)

> 입력값과 정답이 있음

* training dataset(학습data set 있음)

* 세가지로 분류됨 

  * 범위가 넓은 실수를 예측하고자 할때 regressoin e.g. 공부시간에 따른 점수 예측

  * 어떤값 예측 binary classification(분류) e.g. 공부시간에 따른 합불 예측, 신용카드 도난 예측

  * multinominal classification e.g. 공부시간에 따른 grade(a,b,c,d,f) 예측

    => classification은 clustering과 다름!!!! 비지도 학습은 label data가 없고 입력값만 있으며 유사한 입력값까리 묶어주는 거임

### 2) 비지도학습(unsupervised learning)

> 입력값은 있으나 정답이 없음, 분류, clustering 이라고 볼수 있음

### 3) 준지도학습(semi supervied learning)

> 지도와 비지도 학습 섞여있음 일단 clustering 헤서 label 있는애랑 없는 애 분류해서 맞춰준다. 

### 4) 강화학습(reinforced learning)

> game과 금융에서 사용됨 reward 체계에 근거해서 최적의 policy 찾아낸다. 





# 4. 기초미분

### 1) 미분

> 어떤 함수의 정의역  속 각 점에서 독립변수의 변화량과 함수값의 변화량의 비율의 극한으로 구성된 집합으로 치역이 구성되는 함수
>
> 어떤 함수에 대해 특정 순간에 대한 변화량

* 수치미분(numerical differentiation) :  이론적으로 미분 못하는 경우, 프로그램적으로 계산해서 미분 추정, 소수점 아주 작은 숫자 연산 불가해서 약간의 오류 발생
* 해석미분: 연필, 종이 수학식 이론에 입각해서 푸는거
* 미분법(differentiation): 미분을 하는 작업, 도함수(derivative) 구하는 작업
  * 전향차분
  * 중앙차분=> 가장 정확도가 높아서 많이 사용한다. 

![중앙차분 이미지 검색결과](data:image/jpeg;base64,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)
* 후향차분



### 2) 기본 미분 공식

![공식](md-images/formula.png)

* 연쇄 법칙 

  합성함수를 구성하는 각 함수를 각각 미분해서 그 결과의 곱으로 계산

  ![image-20210222165256528](md-images/%EC%98%884.png)

### 3) 편미분

* 독립변수가 2개이상인 다변수 함수에서 미분하고자 하는 변수를 제외한 나머지 변수들을 상수처리해서 미분 진행

![편미분 예시 이미지 검색결과](md-images/R720x0.q80)



### 4) 수치미분 구현하기 

#### (1)

![image-20210222165502738](md-images/%EC%A4%91%EC%95%99%EC%B0%A8%EB%B6%84%EC%9D%B4%EC%9A%A9.png)

```python
#일변수 함수에 대한 수치미분 구현
#입력으로 들어오는 X에서 아주 미세하게 변화할때 함수 F가 얼마나 변화하는 지 추치적으로 계산
#인수를 2개 받는다. 미분하려는 함수, 특정 점에서 미분값 구하기 위한 x값

def numerical_derivative(f,x):
    delta_x = 1e-5
    
    return (f(x+delta_x)-f(x-delta_x))/(2*delta_x)

#미분하려는 단변수 함수

def my_func(x):
    return x**2
result = numerical_derivative(my_func,3)
print('미분한 결과값은: {}'.format(result))
#미분한 결과값은: 6.000000000039306

```



#### (2) 다변수 함수 수치미분

![image-20210222170147906](md-images/ex5.png)



```python
# 입력변수 2개이기 떄문에 x,y에 대한 편미분 진행
import numpy as np
#f:미분하려는 다변수함수
#x: 모든 값을 포함하는 numpy array
def numerical_derivative(f,x):
    delta_x = 1e-4
    derivative_x = np.zeros_like(x) #x의 shape에 값0으로 채움

    it = np.nditer(x,flags=['multi_index']) #x에 대해 멀티인덱스 적용

    while not it.finished:
        idx = it.multi_index
        print('현재의 idx: {}'.format(idx)) #(0,) 1차원으로 나옴
        it.iternext()

    return(derivative_x)

    def my_func(x):
        return x**2

numerical_derivative(my_func,np.array([3]))
현재의 idx: (0,)
array([0])

numerical_derivative(my_func,np.array([1.0,2.0]))
현재의 idx: (0,)
현재의 idx: (1,)
array([0., 0.])

param = np.array([[1,2],[3,4]]) #2차원 matrix
numerical_derivative(my_func, param)
현재의 idx: (0, 0)
현재의 idx: (0, 1)
현재의 idx: (1, 0)
현재의 idx: (1, 1)
array([[0, 0],
       [0, 0]])
```



* **iterator**
  * for 문의 index 값이 =`it.multi_index`
  * `it.finished`, `it.iternext()`는 차원에 상관없이 그 길이에 따라 사용할 수 있어서 자주 사용됨
  * 지시자, 포인터, 가리키는 거, numpy 배열에 있는 요소 가리켜서 사용할 수 있다.  인덱스 가지고 numpy array 사용할 수 있게 함

```python
import numpy as np
#f:미분하려는 다변수함수
#x: 모든 값을 포함하는 numpy array ex) f'(1.0, 2.0) = (8.0, 15.0)
    # 만약 x가 4개일 경우 1차원 벡터가 아닌 2x2 Matrix로 들어올 수 있음
def numerical_derivative(f,x):
    delta_x = 1e-4
    derivative_x = np.zeros_like(x) #x의 shape에 값0으로 채움

    it = np.nditer(x,flags=['multi_index']) #x에 대해 멀티인덱스 적용

    while not it.finished: #it 끝나지 않으면 계속 돌아
        idx = it.multi_index
        print('현재의 idx: {}'.format(idx)) #(0,) 1차원으로 나옴
        
        tmp = x[idx]
        # 현재 index에 있는 값 잠시 저장
        #delta_x를 이용한 값으로 ndarray 수정한 후 편미분 계산
        # 함수값 계산한후 원상복구 해줘야 독립변수에 대한 편미분 정상적 수행 가능
        print('현재의 tmp :{}'.format(tmp))#1.0 #2.0
        
        #x에 대한 편미분
        x[idx] =tmp +delta_x #1.00001
        fx_plus_delta = f(x) #f([1.00001, 2.0]) => f(x+delta_x)
        
        #중앙차분 미분준비
        x[idx] = tmp-delta_x
        fx_minus_delta = f(x) # f([0.99999, 2.0]) => f(x - delta_x)
        
        #중앙차분
        derivative_x[idx] =(fx_plus_delta -fx_minus_delta) / (2*delta_x)
        
        #두번째 독립변수 위해서 복구
        x[idx] =tmp
        
        it.iternext()

    return(derivative_x)

def my_func(input_data):# input_data = numpy.array
    x = input_data[0]
    y = input_data[1]
    return 2*x + 3*x*y+np.power(y,3) # f(x) = 2x + 3xy + y^3
param =np.array([1.0,2.0])
result = numerical_derivative(my_func,param)
print('미분한 결과: {}'.format(result))

```



# 5. Tensorflow

* node와 edge로 구성된 방향성 있는 그래프
* node는 수치연산과 데이터 입출력
* tensor는 data를 실어 나르는 역할을 한다. 방향성 있음
* data는 동적 크기의 다차원 배열 tensor flow
* tensor flow는 그래프 만들어서 실행 시키는 구조 =>구조 그래프 만듬=>내가 원하는 노드 실행시킴