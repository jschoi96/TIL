# AI

## 1. AI

> 인간이 가지는 특유의 학습능력, 추론능력을 컴퓨터로 구현하려는 가장 포괄적인 개념, 그 중 한가지가 machine learning

* data mining: data 간의 상관관계, data feature , 특징들간의 상관관계를 밝히거나 새로운 속성들 알아냄
* AI 는 explicit program(rule based programming)으로 해결할 수 없는 것들을 해결하기 위해 등장 
* 규칙이 너무 많거나, 경우의 수가, 조건이 너무 많은 경우=> machine learning 

## 2. machine learning

> AI를 구현하기 위한 하나의 방법으로 data 이용해서 data pattern을 학습하게 한다. data 특성과 pattern 학습해서 미지의 data에 대한 추정치를 계산

### 1) regression
<img src="md-images/formula2.png" alt="image-20210222170703140" style="zoom:50%;" />

> regression model :어떠한 데이터에 대해서  그 값에 영향을 주는 조건을 고려하여 데이터의 평균을 구하기 위한 함수
> 어떤 연속형 데이터 y와 이 y의 원인이라 생각되는 x간의 관계를 추정하기 위해서 만든 y=f(x)+e(error)
![image-20210224213453499](md-images/image-20210224213453499.png)

* 기본적으로 classical linear regression model 가정함

*  어떠한 데이터에 대해서 그 값에 영향을 주는 조건을 고려하여 그 데이터를 가장 잘 표현하는 함수 

* 주어진 데이터를 가장 잘 표현하는 직선 찾는다. 

* regression toward mean

* 단변량 선형회귀(종속변수의 갯수-1개)

* h는 조건에 따른 평균을 구하는 함수(회귀모델)

  모델은 단순화하기 위해서, 우리가 해결해야 하는 현실은 복잡하기 떄문이다. 

  오차항의 평균이 0, 정규분포

  독립변수와 종속변수가 선형

  데이터에 아웃라이어가 없어야 

  독립변수와 오차항은 독립

* 독립변수의 갯수에 따라 simple linear regression, multiple linear regression

* 머신러닝에서는 `y=wx+b` weight 는 가중치 b는 bias
  * data가장 잘 표현하는 w와 b를 찾아가는 과정
  * error 값을 제곱해서 loss function 찾는다. 평균제곱오차가 최소가 되는 weight와 bias



### (1) loss function(cost function, 비용함수)

![회귀 모델에 대한 성능 평가 지표들](../../../Desktop/%ED%9A%8C%EA%B7%80%20%EB%AA%A8%EB%8D%B8%EC%97%90%20%EB%8C%80%ED%95%9C%20%EC%84%B1%EB%8A%A5%20%ED%8F%89%EA%B0%80%20%EC%A7%80%ED%91%9C%EB%93%A4.png)				

![단순회귀분석 이미지 검색결과](../../../Desktop/%EB%8B%A8%EC%88%9C%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D%20%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EA%B2%80%EC%83%89%EA%B2%B0%EA%B3%BC.jpeg)

* training dataset의 정답(t)와 입력 x에 대한 계산값 y(모델의 예측값)의 차이를 모두 더해 수식으로 나타낸 식

* 최소제곱법: 손실 함수를 만드는 과정

* loss function 과 MSE(Mean squared error)

* 최소제곱법을 이용해서 loss function을 만들고  만든 loss function이 최소가 되게 하는 w와 b를 학습과정을 통해 찾는다. 

* MSE와 loss function은 같은가?

  * 항상 같지 않다. MSE만 가지고 loss function 만들어낼수 없음

  * simple linear regression에서만 같다. 

    

### (2)경사하강법(gradient descent algorithm)

<img src="https://miro.medium.com/max/2284/1*jNyE54fTVOH1203IwYeNEg.png" alt="Gradient Descent Algorithm and Its Variants | by Imad Dabbura | Towards  Data Science" style="zoom:50%;" />

* loss function은 W와 b에 대한 함수로  이차함수이다. 

* 손실함수의 편미분을 통해 손실함수가 최소가 되는 w값을 찾아간다. 

  랜덤의 w를 잡아서 편미분한다. 편미분 값이 0인 지점에서 멀어질 수록 기울기가 커진다. => 편미분 값이 커진다=> w 값이 제일 작은점으로 부터 얼마나 멀리 있냐에 따라  업데이트되는 w가 달라진다. 멀면멀수록 W에서 많이 빼줘서 더 많이 움직인다. 일반적으로 편미분 값이 커서 `learning rate`곱해준다.

  ![image-20210224160937236](../../../Desktop/image-20210224160937236.png)

* loss function 이 최소가 되는 w를 찾기 위해 사용된다.

* `hyper parameter`: 사용자가 직접 customize 해야 하는 값
  * `learning rate`: data size , 컴퓨터 사양, model 에 따라 내가 알아서 customize 해야함 알파 값으로 0.001~0.0001부터 시작
    * 발산: learning rate가 너무 크면 최적의 w 뛰어 넘는다. 
	* `epoch`: w와 b 몇번 업데이트 시킬것인가. 몇번 학습시킬 것인가. 많이 학습시키면 좋을 것 같지만 overfitting 문제가 생긴다. 
  	* `overfitting`:  학습 반복수, W와 b가 없데이트 많이 될수록 내 training set에 너무 비슷하게 되서 결과적으로 예측에 부적합해진다. 



<img src="md-images/selection_of_learning_rate.png" alt="쉽게 배우는 경사하강 학습법 | DataLatte's IT Blog" style="zoom:25%;" />

* 손실함수는 모델 성능 평가에 사용되지 않음. 학습에 사용됨

![simple linear 정리](md-images/simple%20linear%20%EC%A0%95%EB%A6%AC.png)

* simple linear regression code 구현 python, tendorflow, sklearn



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

![중앙차분 이미지 검색결과](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxATEhUPEA8VFhUWFxUWFxgYGBYXFxAZFRUYFxgYFhUeIiggGB4lGxcYIj0hJSktLi4uGB8zODMtNygtLisBCgoKDg0OGxAQGy8mHSUvLi0tLjctLS0uLy0vLS0tLS8rLy8tLS0tNS0tLS0tKysuKysvLS4tLS0tKysrLS0tN//AABEIAKUBMgMBIgACEQEDEQH/xAAbAAEAAwEBAQEAAAAAAAAAAAAABAUGAwECB//EAE0QAAEDAgQBBggKCAQEBwAAAAEAAgMEEQUSITETBiIyQVGBFlVhcXORk9MHFDVCUlNylLHCFSMlMzSCobNDYmOSJKPS8ERUZKKyw9H/xAAYAQEBAQEBAAAAAAAAAAAAAAAAAQIDBP/EAC8RAQACAQIEAgkEAwAAAAAAAAABAhEDMRIhQVGR0SIyUmFxscHh8BOBkqEEFCP/2gAMAwEAAhEDEQA/AP3FERAREQeErnS1LJGCSJ7XscLtc0hzXDtBGhSr6Dvsu/BZf4KPkij9F+ZyDWoiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIqinxjPVyUrGXbEwGR99Gvd0WAdZtqrdSJy1as13ERFWRERAREQEREBERAREQcqvoO+y78Fl/go+SKP0X5nLUVfQd9l34LL/BR8kUfovzOQa1ERAREQEREBERAREQEREBERAREQEREBERAREQFVcpMXFNA6W2Z5syNvXI92jQP++pWhKyeF/8AG1RrDrTwFzKcdUj9ny26wNh3rNp6Q7aNImeK3qxv9I/da8mMKNPDlec0ryZJXfTkfqe4bdyuERWIw53vN7TaeoiIqyIiICIiAiIgIoj8ShDnRulaHMbncCeg3tcervUoO60wPUXl18xytcLtIIuRob6tNiPOCCO5B81fQd9l34LL/BR8kUfovzOWkq522czMMxY9wF9SALEgdmo9azfwUfJFH6L8zkGtREQEREBERAREQEREBERAREQEREBERAREQEXipuUuMmBjWRNzzynJCz6Tj84/5W7kqTOGqUm9uGEDlJVvnkGGU7iHOAdUPH+BEeq/U52w9a0VFSMiY2KNoaxgDWgdQCruTeD/ABeM5nZ5ZDnlkO73n8ANgFcKVjrLrq3jEUptH9z38hERacBERAREQEREBERBkMRwh7ZKmoyOLXS0r7BxdnZGWmSzLnYi9rdVgpFDQ1Xxh8hzCFxlMILw7gOcBz3Nvz2uNyG3OW9tL6aayWXT9WcYTCghgrYoJQX8WRznZLBrSwOe7nXc6xsCDlvpayiCilayWGGllbG+PQGSJrmyts0OD2vJGYWcT2tJ1Llq0U45MMfHSVDeE2YOdM2SaSSW92vj4Lm3b9AHMxuTTVpOu65fBVA/9FUzuM6zoua2zLQ852rTa7v5iVr6voO+y78FmPgo+SKP0X5nJa8yYXzaObhlhqnl5NxJkizNGmgblynr3HWklHMY2sFU8OB1kDIsz99C0tyjcbDqU9FnKoklNIXMcKhzQ22ZobGRL5yW3HdZGU0gkMhncWHaPLHlboNnBub1nrUtEyIMFJKA8OqnuLuiS2IcLfVtmi+46V9l4aObhhnxp+e9+JkizEdmXLl/p1KeiZEGeklIYG1L25ekQ2I8XbV12m23zbbr6lpZTIHioc1gteMNjLXW35xbm18hUxEyIkdNIJC8zucw7RlsYa3bZwGY95618RUcwY5pqnuc7ovLYgY/MA2x7wVORMiC6jmMYYKp4eDcyZYszhroW5co3Gw6vOlRSTODMtU9mUWdZsR4h01OZpt3W3U5EyIklNIZA8VDgwbxhsZa7fdxbmHcepIqaQSOeahzmm9mFsYazss4NzG3lPWpaJkQaejmaHh1U95cLNJbEDEddQA0A7je+y8NHNwwz40/Pe/EyRZiOzLly/0vop6JkQZaOYsawVT2uG7w2ImTfQgtyjuA2X3LTSGRrxUOa0WvGGxlr7E3JcW5he/UepS0TIg/FJeJxPjT8l78PLFlta1s2XN5d19RU0okL3VDnNN7RlsYa2/Y4NzG3lK61dVHG0ySPDWjck2CymNconujMjXGCAmwkIvNUH6MEfl7T51m18M59KK1jMz0SsYxltKx8b6t8kr+gA2LPGTtoG2/3AnzrlySopDPNUVXOqG8Nlz/AIbXRtflAAAaecL2G4XLkdyZyu+O1LDxXasY4l3AB63E7yHrJ28iu8K/iKv0kX9iNKZtEzZu1LUt63Prjb4e9bWXqIqgiIgIiICIiAiIgIiICIiAiIg5VfQd9l34LL/BR8kUfovzOWoq+g77LvwWX+Cj5Io/Rfmcg1qIiAiIgIiICIiAiIgIiICIiAiKJiGIRQs4krw0f1cewDclEmYiMylKmxDHg13Ap2Gab6LTzWeWR+zR/VRf+Kq/pU8B7ppR/wDWP6qPPiUcB+I4bAJJ/nW6EN/nzSdvk3WJszSuprTinKO/585ccSDIcs9c8zzuNoYGDm5uoMj67fSKm4LgsrpBW1xDprfq4x0KVp6m9ru1ykYHyfETjUTv41S7pSH5g+jGPmN8yvUivd6I4NGJrp7zvbv8Pzm8CqsK/iKv0kX9hitlTYfIGz1r3Gwa+Mk9gFOwkrrG0/nVyXKLKYTy6p5o2S5S1r+M+5c0iOGC2aWU7MF3NGXU87sBtfNxWnIkcJmERAOkIIIjBbnBcerm6+YrImooWL4mynhdO8OcBYBrBd8rnENYxg63OcQAPKvkYzTZY3mZgbK0vjJNhI0Nzki/Y3XzIJ6KtwvGYp3PYy92BjgdLSxytzRyMI3abOHnaVU1HLWBs1RAGOcafhNOUtzSyzOa2OKNhO5c9ozEgAnvQahFAgxine5sbZmF7jI0NDgXXiIEgtvzSQD2XHavjHMaipWCSXMQXBoDRd3WXOt9FjA55PU1p32QWSKBV4zTREiWdjCIzLznAfqwQC8douQO8dq9wrE2zh9mua6OR0b2utdpbYg6Eizmlrh5HC9jcIJyIiAiIgquVFfJBSyzRNBe1txfYdVyOu29lAbjkkbZHzglkHCjkPNzNc5jXPkdbQgZ2izfKexX1ZSslY6KRuZjhYg9YUSTB4nSOkcL5ixxaeiXx6NfbrNrDXTmjsXStq4xMIhRYq97g1zMrJoHyRg2zNyEA5rac5r2G3Vr3VHwT10P6Jpm8Vl44ryDM28QzON3i/N07VoBhEUeZ7ARaJzGN+bGCS52Xzm3+0AWVN8E7B+iKPQaxa+XnO3WbcPQaGDFqZ7XPjqInNYLvLZGODBvdxB5o0O/YjMWpjGZhURGNps54kYWNOmhdewOo08oUoRtGzRrvoNUETbWyi3ZYWU5KizYtTMa2R9RE1rxdjnSMDXje7STZ3clRi1MwNfJURMa8XaXSMaHje7STqNRt2qUY2nQtGm2g0R0bTu0abaDROQi1eLU0VhLURR3FxnexuYdoudR5V9y4hC1zGOmjDn9Bpe0Okv9EXu7uXd0TTu0HuC9LBvYababJyEdmIQmQwNmjMg3YHtL27bsvcbj1hfMOK07w8sqInBmry17CI9+mQebsd+wqUGC97C/bbX1rwRtGzRrvoNU5CK3FqYxmYVERjabOeJGFjSbCxdewOo9YSbFqZjWyPqImteLsc6RgbIN7tJNnbjZSuG21sot2WFkMbdi0abaDROQjVGK07MvEqIm5xdmZ7W5xpq2552427V9PxCESCF00YkOoYXtD3b7Mvc7H1Lu6Np3aNPINF6WC97C/bbVOQjx4hC5z2NmjLmdNoe0mO30xe7e9fEOLUz2ukZUROYzpOa9haz7TgbDvXPE8SgpxmkIu7QNAu+Q9gbuVTyU0s7S+qIpqbcxggOeP9V+zR5AszaIc7X58Necu2JcqGC7aYseRbNK5wbBDfQZ5NjrbQHVcRFS05FTXVbHy2zBz3AAD/Rj7NtQCVxZjWdvxfCqUSNGnEcMtPH5b7yHzJNyXjymoxCodLIMtn2syDntIEcYvbWwupXEzzdo/wAXHpa88+kfb6z4PfjFZX6Q5qamO8hFppx/pg9AHtOq0GEYTDTs4cLMo3J3c89rnbkqavUiuObpfWm0cNYxXt59xERacRVGFfxFZ6SL+wxW6qcK/iKv0kX9hi1G0/nUVNNyYmg4Ap5mnJBNTuc9t7CRweyQM2cWuFspOodvpY/NFyDp2UkmHl7nQOOaMHR8LjHkcc4Iz6kuAI0vbYADXIsihnwBwMAp5GMZBnLWPY+UF77jPfiNNwHPAuSOeewWrcQ5FOnhNNPVDhcWSYNjiDcjnNOUNLnPs0Pc59uu+Xo807BEGbp+T7pJJpKwteHx08IDczM7YMzy8gG7S58juaCQA0a6rlinJdx40sDxxHS0k8bXaNDqQMAY52ps4MtmtpmvrZalEGYpOSQFRNVvlzGoa9k7Moa17Dl4bWEG7C0CxdfnXN9m2kSYDI2Rr4JYmsZFwmRyRPlEYcbvIPEbcus0a30b5Te/RBjqnkU+RsDZKvWlu6AtiFmP4gcwuDnOL2ta0MDb6jUkkAi7wLD5I3VE0pGeeYvs03DGtY2JgvYalrAT2F1tbXVsiAiIg8uiz/K6lfIKdjXENNQwPAaHAtyvPOHYCBvpqFVOxKpjj4kV3yvlquK0sLuG1j3NDwBrzGtZZnzx5TddK6eYzEpMtsvLqoqcSlijfI5gc0Nbw3ZiXTOdYDOwNAYLne50vsquKvdFHLE2pc92QyskymQ57jOwt7C83DexxAtlUikyZaar6Dvsu/BZj4KPkij9F+Zy+I62Z/CklBZK6SaN8VrCOMQuda/zwC1js/a6wtsuPwU8f9EU1uH+6HD6W+Z1+J322UtThMtsigR/GuG7NweJfm2z5LadLr7dvIh+NcMW4PFvr08ltduu+ymFT0UCf41lZw+Dntz82fLf/JbXt3XSXj525eHktz75s1+vL1dm6YEtFEi+McR2bh8PXLbNnvpbNfTt/ovin+NWfxODe3My57X16d+rbbypgTkUCH41kdn4Of5mXPl/mvr6kj+NcN2bg8T5ts+S2nS6+3ZMCeioa7G+BE41FTSskvzbudltpe4vmvvt5FWO5WVEjWiipTO+/PcWPjhtr0HutfqUzG2XWujqWjMRy79PFr3vABJIAGpJ2Cy2L8q22IgexrRo6eTSNvkjG8rvIAq2uwzE67OyWWOAMLQWNzOa67GvuHfO6VuwEFSsL5IvhIcI6Z7xs+UyvcPNfRvcApatp5Q5VrFs8czEe7ef32j+0TDJpHuz0dK+aR29VU3jYPRtPOt5AAriHkrxCJMQndUuGoZ0YGHyRDR3nddTwK//ANN6pV7+0O2m9UqRpx1l1rqxpxjSrw/Px8sLOKJrQGtaABoABYDzBccQaTGQIhJ0eYbAO5w7dNN+5Qv2h203qlULGW4iYXBvBvdn7vi5+m3bu/pdbivPdymWiC9VT+0O2m/5qftDtpvVKnD7xbIqn9odtN6pU/aHbTeqVOH3i2VThX8RV+ki/sMT9odtN6pV8YFDOJal07WgufGQWh2VwELBzb6nUWViMRPNFyiIsKIiICIiAiIgIiICIiAubImgucGgFxu4gWLiABc9ugA7l0Xy5t9EHt0WbPIei7Jvbzf9S88Cqf8A8xV/eJP/ANWcz2d+DR9qfD7r2riblc/KMwY4A21AI1APZoPUs38FHyRR+i/O5dKjkZAGuPHqtAT/ABEnZ51Q/B7yYp6jDqaeYykvjvlbLIxjOcRzGNIDRombdl4NH25/j936Ndc3VDBqXtHnICoByHofoynyGaYg+cZtV9s5E4cP/CMPnLiPUSnpJw6PtT4R5rKbGKVl89RELam726f1UCbljhzd6uM/ZJd/8QV2h5LUDLZaKHTbmNJHeQrCGhhZ0ImN8zWj8AnpH/CO8+Eeai8NKc/uoamX7EL7HvdYL5OP1z/3OFSeeWRkY7wMxWmASyYnufqacbU8Zn6YZgRYxJ0pKWAf5Q+V49dgvfBN8n8ViFRL2tDhEw/yt6u9aZepwx1X/ZvHqxEfCI+e6ow/kzRQm8VNGHfSIzO/3G5VsAvUViIhxte15zacotNxc8ue2TM3h2t0cjc1/wCfMpShUbGiSYiUuJe27fqTw2DKOy4s7+ZTVqWRERQFCxcS8J3A/eXba1vpjNvp0bqaoeKxudE5rZeGbt597ZbOB303271Y3ExERQEREBQ6RsvFmLzzC5nC20HDbm/9191MUKkY0SzESlxLmXb9T+raAB2XFnd6sCaiIoCIiAiIgIiICIiAiIgLO41yWdUSmYYlXQ3AGSGWNsYt1hpYTc+daJEGP8BXeOsU9vF7pPAV3jrFPbxe6WwRBi6jkM4Mcf01ifRO80Vjp6JUHwdckHTYbSy/pXEIs0d8kcsbY2c52jQYyQO9fp1X0HfZd+Cy/wAFHyRR+i/M5B8eArvHWKe3i90ngK7x1int4vdLYIgx/gK7x1int4vdJ4Cu8dYp7eL3S2CIMf4Cu8dYp7eL3SeArvHWKe3i90tgiDH+ArvHWKe3i90ngK7x1int4vdLYIgx55DO8dYp7eL3S88B3eO8T9vF7pa6Zt2kZQbg6HZ2mx0Oncs3gnJ2aIPa+XLmDLPiPPjDb/qG52kcJt9DvqdAtREYmcisfyMZG8NON4k18pNhxoQZS1uv+FqQ0D+ik+A58d4n2fv4vdKwrsNqXuldkiJOURO4rwYQwhzTbhnXPqdddB1Ll+hJ3VTap4hABjzxhzy17msIM18o57SbDTYakG1tcMTvKIvgK7x1int4vdJ4Cu8dYp7eL3S14Xq5qx/gK7x1int4vdLnNyCzDK/GcSIPUZoSDY324XatoqblLhUlQxjI3NYQ/NxNc8XNI/Vgbk3ym5GhK1XfcU45DO8d4p7eL3S98BXeOsU9vF7paXC6cxwxxljGFrWtLWEljbDZpIBt5wpazIx/gK7x1int4vdLx3IZwFzjeKW9PFp/ylsV8yXsbAE+XY+dBjW8i77Y7iRuM38RDqO391t5VzdyIawPm/TWJAEZ3u40PODW7k8LXmhWeEcmnxNlY6TSQNOaMuY6Igk8Nh6ohfQdV3dq6twmRsMVNHIJBG5nED3u5+RoIYCA7K3MGnL2C3WukxWNpRT0/JFr2skbjuJ5XgFv6+IZri9gDFv5F2ZyJJF243iZG2k8J23/AMJTarA55GPiJjja+VsgLHOc+A7vMZLW2JcLjsLneZXGEUrooY4nBgLGhvMBDTbS4B2vvZSYjGYkZzwFd46xT28XulZ4BycdTPc84hWVGZuXLPIx7W6g3aGsbY6W361eosKIiICIiAiIgIiICIiAiIg5VIuxwH0Xfgs38GED48KpI5GOY4R6tcC1zec7cHULUogIiICIiAiIgIiICIiDIUHKFkU9bHKyqeRUc3h09VO1oMEOgfGxzRrc5b9flVh4W0/1Fb9xrvdKdhWHmJ9Q4uB403FFvmjhRsse9hPerFBQeFtP9RW/ca73SeFtP9RW/ca73Sv0QUHhbT/UVv3Gu90nhdT/AFFb9xrvdKDy/rzGxkcVTJHUScQQMY6JokcAOfK6RpAjZcE9t7WJsF94pidSXtZTyMLqdjJZ7WtUucNIGX2zNzvuDcERdTigl+FtP9RW/ca73SeFtP8AUVv3Gu90qys5ZEVMFPCI3sqWwvilu7LC2Qm/GHUXgWYNMzrjS1zsQgofC2n+orfuNd7pPC2n+orfuNd7pX6IKDwtp/qK37jXe6UbkVVNlkr5WNeA6rGj2PifpSUw50bwHN26wtQoOHYa2J88gcSZ5RKQbWaRFHFYeS0YPnJQTkREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREHCopIpLcSJj7bZmh1vNdcpMLp3G7qeIntLGk+uyIg+20MIBaIWAG1wGtscvRuLdSkoiAiIgIiICIiAiIgIiICIiAiIgIiIP//Z)
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

* numerical computation(수치연산)
* node와 edge로 구성된 방향성 있는 그래프
* node는 수치연산과 데이터 입출력
* edge는 data를 실어 나르는 역할을 한다. 방향성 있음, edge를 통해서 데이터가 한 노드에서 다른 노드로 옮겨간다
* data:  동적 크기의 다차원 배열 tensor라고 한다. 
* tensor flow는 그래프 만들어서 실행 시키는 구조 =>구조 그래프 만듬=>내가 원하는 노드 실행시킴





reference:   [ML_0223.ipynb](..\..\..\..\..\python_ML\ML_0223.ipynb) , [ML_0224.ipynb](..\..\..\..\..\python_ML\ML_0224.ipynb) 