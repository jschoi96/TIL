# 1. pandas

> `numpy`를 기본으로 해서 자료구조 2개 더 정의-`Series`와 `Dataframe`

* `Series`를 여러개 합치면 `Dataframe`이 된다.  
* `Series`는 `dataframe`의 column



# 2. series

> 동일한 데이터 타입의 복수개의 성분으로 구성

* `numpy`의  `ndarray`에 +알파
* 같은 데이터 타입이 들어와야 한다. 1차원 numpy 벡터 확장판 **index 값** 가지고 있다. 
* 항상 **1차원**이다.
* 만드는 방법-`list`, `dict`

```python
#Series- pandas의 series class
s=pd.Series([1,2,3,4,5],dtype=np.float64)#pandas의 series class
print(s)
#인덱스 값
#0    1.0
#1    2.0
#2    3.0
#3    4.0
#4    5.0
#dtype: float64 #데이터 타입
값은 value
print('Series의 값만 가져오고 싶어요 :{}'.format(s.values))
#[1. 2. 3. 4. 5.]
print('Series의 index만 가져오고 싶어요 :{}'.format(s.index))
#RangeIndex(start=0, stop=5, step=1);range 의미를 표현하는 설명식
```

```python
#series는 list와 dict로 만들 수 있음
my_dict={'서울':1000,'인천':2000,'수원':3000}
s=pd.Series(my_dict)
print(s)
#키 값이 index로 사용
# 서울    1000
# 인천    2000
# 수원    3000
# dtype: int64

s.name='지역별 가격 데이터' #series 이름
print(s)
print(s.index)
# index class타입 개체, 사용방법은 리스트와 유사

s.index=['Seoul','Inshon','Suwon'] #요롷게 하면 인덱스 바뀜
s.index.name='Region'
print(s)
```



### 1) index

* index는 순서가 있다는 뜻
* `numpy` index는 숫자 밖에 없음. `Series`의 index는 원하는대로 지정가능

```python
s=pd.Series([1,5,8,10],
            dtype=np.int32,
           index=['a','b','c','d'])
print(s)
#a     1
# b     5
# c     8
# d    10
# dtype: int32

s=pd.Series([1,5,8,10],
            dtype=np.int32, 
            index=['a','b','c','d'])
print(s)
```

* indexing

```python
print(s[1]) #5 인덱싱 새로 만들어줘도 기존 인덱싱 작동
print(s['b']) #5 만든 인덱싱으로도 인덱싱 가능

s=pd.Series([1,5,8,10],
            dtype=np.int32, 
            index=['a','b','a','d'])
result=s['a']
# a    1
# a    8
# dtype: int32
print(type(result)) #<class 'pandas.core.series.Series'> series야

#fancy indexing (안에 리스트 형태의 index 배열)
print(s[[0,2]])
# a    1
# c    8
# dtype: int32

#boolean indexing
print(s[['a','c']]) #=>가능
print(s[s%2==0])
# c     8
# d    10
# dtype: int32
```



* slicing
  * 가능 하지만 지정한 index의 마지막은 inclusive 

```python
print(s[0:3]) #슬라이싱 결과가 원본과 같다. 그대로 적용
# a    1
# b    5
# c    8
# dtype: int32

#지정한 index(도 가능?=> 가능 하지만 'd'도 inclusive
print(s['a':'d'])
```



# 3. dataframe

> table 형식으로 데이터를 저장하는 자료구조

* 만드는 방법
  * dict를 이용해서 수동으로 만드는 방법
  * CSV를 이용해서 파일로부터 데이터를 읽어들여서 DataFrame을 만드는 방법
  * 기존 Database로부터 데이터를 읽어서 DataFrame을 만드는 방법

```python
my_dict={'name':['홍길동','신사임당','최지수','최지윤'],
         'year':[2015,2016,2019,2020], #하나만 빠져도 에러난다. # 값없으면(PYTHON)None 주던가=(PANDAS)NaN
        'point':[3.5,1.0,4.3,4.2]}
s=pd.Series(my_dict)
print(s)
#value값의 갯수 같아야

df=pd.DataFrame(my_dict)
print(df)#삐뚤빼뚤 출력할떄 print 보다 display
display(df)
#key값이 column명
print(df.shape) #4.3
print(df.size) #12 size는 값싹다 몇개 
print(df.ndim)  #2
print(df.index)#RangeIndex(start=0, stop=4, step=1)
print(df.columns)# Index(['name', 'year', 'point'], dtype='object')
print(df.values)# 2차원 numpy
# [['홍길동' 2015 3.5]
#  ['신사임당' 2016 1.0]
#  ['최지수' 2019 4.3]
#  ['최지윤' 2020 4.2]]
```

* 직접 `dict`작성해서 만드는 방식은 적은 양의 데이터 처리에 적합, 많은 양의 데이터는 (1) 파일, (2) database, (3) open api를 통해서 얻어야 함

```python
#csv 파일 여는 방법
df=pd.read.csv(./movies.csv)#.이 의미하는 거는 주피터 노트북 폴더랑 같다.
display(df.head())
```



#  4. 예제문제

A공장의 2020-01-01부터 10일간 생산량을 Series로 저장
날짜를 처리하는 datatype이 따로 있다.=>외부 모듈 가져와야 datetime(pip install)
생산량은 평균이 50이고 표준편차가 5일 정규분포에서 랜덤하게 생성
형식) 2020-01-01 52
     2020-01-02 49
     2020-01-03 55
=>인덱스를 날짜로


B 공장의 2020-01-01부터 10일간 생산량을 Series로 저장
생산량은 평균이 70이고 표준편차가 8일 정규분포에서 랜덤하게 생성
날짜별로 모든(a공장,  b공장)의 생산량의 합계를 구하세요



* 날짜 연산 `datetime`이라는 모듈 필요하다. 일단위 증감=> `timedelta`, 월, 년단위 증감  =>`relative delta`,주 단위 증감도 가능
* list comprehension 에 대한 이해 필요

```python
#import datetime하면 안됨
from datetime import datetime, timedelta
start_day=datetime(2020,1,1)
print(start_day)#2020-01-01 00:00:00
factory_A=pd.Series([int(x) for x in np.random.normal(50,5,(10,))],
                    dtype=np.int32,
                    index=[start_day +timedelta(days=x) for x in range(10)])
					# x2번 ㄱㅊ list만들면서 x scope 끝
print(factory_A)

start_day=datetime(2020,1,1)
factory_B=pd.Series([int(x) for x in np.random.normal(70,8,(10,))],
                    dtype=np.int32,
                    index=[start_day +timedelta(days=x) for x in range(10)])
print(factory_B)

print(factory_A+factory_B)
#SERIES를 더할때는 같은 인덱스에 한해서 더하기 해준다. 
#index 다를 경우 NaN not a number index
```

