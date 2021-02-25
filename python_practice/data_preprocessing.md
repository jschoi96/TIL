# Data preprocessing

머신러닝에서 학습이 잘되기 위해서는 양질의 data가 있어야 한다. 

데이터 전처리에는 크게 **이상치 처리** , **정규화**, **새로운 feature 찾아내기**, **feature 삭제하기**가 있다. 

# 1. 이상치 처리

> 속성안에 들어 있는 값이 일반적인 값에 비해 편차가 큰 값을 지운다. 

* 이상치 때문에 전체 데이터가 불안정해지고 이상치에 가중치가 많이 부여된다. 전체 데이터의 신뢰성이 떨어지고  데이터 오염
* 독립변수에 있는 이상치는 `지대점`
* 종속변수에 있는 이상치는 `이상치`
* 이상치를 처리 혹은 검출 할 수 있는 알고리즘 혹은 방법 알아야 한다. 

## 1) 이상치 검출방식

* variance: 정규분포 이용
* likelihood: bayes 정리 활용하고 이상치 발생확률 계산
* nearest-neighbor: 모든 데이터 쌍 간의 거리
* density: 카이제곱검정 이용

이중 `tukey fense` 랑 `z score`

* `tukey fense`: 4분위 활용하고 boxplot 이용해서 확인가능

  ![image-20210225225448130](md-images/image-20210225225448130.png)



```python
data = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,22.1])

fig = plt.figure()
fig_1 = fig.add_subplot(1,2,1) 
fig_2 = fig.add_subplot(1,2,2)
fig_1.set_title('Original_data')
fig_1.boxplot(data)

#numpy 이용해서 4분위수 구하기 percentile()

print(np.median(data))
print(np.percentile(data,25))
print(np.percentile(data,50))
print(np.percentile(data,75))

#1QR value (3사분위 값)-(1사분위값)
iqr_value = np.percentile(data,75) - np.percentile(data,25)
print(iqr_value)
lower_fense = np.percentile(data,25) - (iqr_value*1.5)
upper_fense = np.percentile(data,75) +(iqr_value*1.5)
print(lower_fense)
print(upper_fense)
result = data[(data <= upper_fense) & (data >=lower_fense)]
fig_2.set_title('remove outlier')
fig_2.boxplot(result)
fig.tight_layout()
plt.show()

```

![img](data:image/png;base64,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)



* `zscore`: 정규분포,표준편차 이용

![image-20210225233737512](md-images/image-20210225233737512.png)





# 2. 정규화(normalization)

> data feature의 scale에 차이가 있는 경우

![그림1](md-images/%EA%B7%B8%EB%A6%BC1.png)

feature 중에서 방갯수 차이는 아파트 연식 차이보다 그 차이가 중요하다.  똑같이 5차이 나더라도 가중치가 더 크다. 똑같은 scale로 맞춰줘야 한다. `normalization`