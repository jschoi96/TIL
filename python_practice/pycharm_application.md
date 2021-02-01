# application 설계하기

* 프로젝트: 개발대상이 되는 전체 프로그램, 
* 어플리케이션: 프로젝트를 몇개의 하위 기능으로 나누었을 때 서브 프로그램을 어플리케이션

![image-20210128234314909](md-images/image-20210128234314909.png)

# 1. 개발 로직 설계

![image-20210128152455993](md-images/image-20210128152455993-1611815200009.png)

* 결국, 화면 UI는 `index.html`,`detail.html`,`result.html` 이렇게 3개 필요
* 테이블은 question table과 choice table 필요



# 2. 프로젝트 뼈대 만들기



## 1) anaconda **prompt**를 열어-project, application 생성

```python
(base) C:\WINDOWS\system32>cd..##base 환경이라는 거 확인 디렉토리 확인

(base) C:\Windows>cd..
  
(base) C:\>django-admin startproject mysite # 프로젝트 시작해줌

(base) C:\>cd myysite

(base) C:\myysite>python manage.py startapp polls#만들 어플리케이션 파일 만드는 과정
    #manage.py 파일은 장고의 명령어 처리
```



## 2) 프로젝트 파일 설정 변경하기

* allowed host, installed apps, database engiene, timezone 설정 확인하고 변경해줘야 한다. 

```pycharm
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
##요 부분은 기본적으로 최상위 폴더로 세팅된다. BASE_DIR이라는 변수를 설정

DEBUG = True #true 이면 개발자 모드, false이면 운영모드

ALLOWED_HOSTS = ['localhost','127.0.0.1']#요롷게 설정

프로젝트에 등록되는 모든 어플리케이션은 설정파일에 포함되어야 한다. 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig'
]


#templates 설정
#장고에서는 템플릿 파일을 찾을 때 settings.py의 template와 installed apps에서 지정된 디텍토리를 검색
#왜 polls/index.html 이렇게 해야 하는 것인가. 어플리케이션은 다르지만 템플릿 이름이 동일할 수 있어서 templates 디렉토리 안에 어플리케이션 명으로 디텍토리 만들어 템플릿 파일을 위치시킴

 template 어디있는지 프로젝트의 템플릿 base dir이 프로젝트 루트...걱
        'APP_DIRS': True, #application 마다 template 폴더 만드는 거 허용
        TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 사용하는 데이터 베이스에 따라서 설정해줘야 한다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        
    }
}

TIME_ZONE = 'Asia/Seoul'

```



* migrate: 데이터 베이스에 변경사항이 있을때 이를 반영해주는 명령어, 변경이 있지 않아도 이 명령 실행하면 데이터 베이스 파일 만들어 준다. 왜냐하면 장고는 모든 웹 프로젝트 개발 시 반드시 사용자와 그룹 테이블이 필요하다는 가정하에 설계되었기 때문에 테이블 안 만들어도 프로젝트 개발 시점에 이 명령 실행

![image-20210128164028225](md-images/image-20210128164028225.png)

* runserver: 개발과정에서 현재 상태를 확인해 볼 수 있도록 runsurver하는 테스트용 웹서버 제공 

```python
python manage.py runserver --이렇게 해줌
```

![image-20210130110942632](md-images/image-20210130110942632.png)







## 3) 모델 코딩하기

* polls>migrations>models.py 파일에서 수행
* 장고에서는테이블을 하나의 클래스로 정의하고 테이블의 컬럼은 속성으로 연결해줌
* 테이블 class는 `django.db.models.Model`클래스 상속받아서 정의
* 결국은 ORM 형태로 database 접근, 테이블 관리 하겠다는 뜻
* 테이블 새로 만들때는 `models`, `admin` 다 수정해줘야 한다. 

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') #date published는 단순 설명
    def __str__(self):
        return self.question_text #객체를 문자열로 표현할때 원래는 데이터 저장 위치가 리턴된다.

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    #id는 자동으로 붙는다. 연결되는 링크 구조, foreign은 종속 개념 원본 primary 키 삭제되면 따라서 삭제
    #constraint 원본 primary 원본 삭제하고 싶으면 foreign 키에 있는 거 지워라
    #cascade option 원본 삭제 원래 안된다. 지울거면 연관된 foreign 키 걸려있는거 같이 지움
    #무결성에 영향을 받지 않고 데이터 베이스 사용할 수 있다.

    def __str__(self):
        return self.choice_text
```



## 4) admin.py에 등록하기

* admin 사이트에서 우리 테이블 보려면 테이블 class 등록해줘야 한다. 

```python
from django.contrib import admin
from polls.models import Question, Choice


admin.site.register(Question)
admin.site.register(Choice)
```



## 5) 데이터베이스 변경사항 반영

* 아래에 터미널 하나 더 열어서  테이블 신규사항, 정의와 변경 등 데이터 베이스에 변경이 필요한 상황이면 실제로 이를 데이터 베이스에 반영해주는 작업이 필요
* 데이터 베이스에 잘 반영이 되었는지는 dbbrowser for sqllite 실행시켜서 알아볼 수 있다. 

```python
(base) C:\makedjangowebsite>python manage.py makemigrations

(base) C:\makedjangowebsite>python manage.py migrate

```

* 잘 실행되었는지는 `http://127.0.0.1:8000/admin`

## 6) URLconf 설계

![image-20210128233818828](md-images/image-20210128233818828.png)

* 설계한 3개의 페이지를 실제로 보여주기 위해서는 `URL`,`View`,`Template`을 연결(mapping)해줘야 한다. 

* URL과 View의 mapping을 URLconf 라고 하며 urls.py에 저장됨

* URLconf 관리하는 방법은 크게  website 혹은 mysite 안에 들어가 있는 urls.py에서 관리하는 방법이 있다. 재사용성, 유지보수성을 위해서 application level urlconf 따로 관리하는게 좋다.

* ```
  #url pattern의 일부 문자열을 추출하기 위함 <int: year>=> /articles/2018이면 괜찮은데
  #/articles/post/이면 매치되지 않음
  ```

* mysite level

  ```python
  from django.contrib import admin
  from django.urls import path,include

  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('survey/', include('survey.urls'))
  ]
  ##url 관리를 다른 애한테 위임할께..application 단위로 url 관리 
  #include,,:~를 포함해서 시작하면 ~로 넘겨 polls로 시작하면 넘
  ##request 항상 여기서 처리 클라인트의 request 항상 여기서 처리,첫 요청 여기서 받음
  ##한곳에다가 url 다 설정하면 어플리케이션 url 설정 매우 복잡해진다
  # 각 어플리케이션 마다 따로 관리해준다.
  ```

* application level

```python
from django.urls import path
from . import views
app_name = 'survey'
#
urlpatterns = [
    path('', views.index, name ='index')
]
#''는 mysite에서 잡아줘서 안써줌
#다른 파일에서도 index 있을 수 있으니까 namespace주게됨 polls:index 이렇게 줘야 한다.
#~요청들어오면 이렇게 처리해

#url을 계층구주로 관리하려고
#이름 가지고 역으로 URL 유추하는 거
```



## 7) View 설계



```python
from django.shortcuts import render

from polls.models import Question

def index(request):
    question_list = Question.objects.all().order_by('-pub date')[:5]
    #Question 테이블 객체에서 pub date 컬럼 기준 역순으로 정렬하여 5개의 최근 question 객체 가져와서 만들어라
    context = {'q_list' : question_list}
    #템플릿한테 넘겨주는 방식은 파이썬 사전 타입으로 변수명과 변수명에 해당되는 객체 context 변수에 넣어 render 함수에 보내줌
    return render(request, 'index.html', context)
    #render 함수는 템플릿 파일에 context 변수를 적용하여 사용자에게 보여줄 최종 html 텍스트 만들고 이를 담아서 httpresponse 객체 반환
```



## 8) template 설계

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {% if question_list %}
    <ul>
        {% for question in question_list%}
        <li><a href="questionnaire/{{question.id}}/">{{question.question_text}}</a></li>
        {% endfor %}
        
        ##question_list를 순회하면서 question text를 보여준다. url 링크는 /questionnaire/1이렇게 인덱스
    </ul>
    {% else %}
    <p>no question available </p>
    {% endif %}
</body>
    
</html>
```



`template tag`

```html
{% for%}: 파이썬 로직
<ul>
    {% for athelete in athlete_list%}
    <li>{{athlete.name}}</li>
    {% endfor %}
    
</ul>
=> athlete_list에 들어있는 항목 athlete를 순회하면서 운동선수의 이름 athlete name 보여주는 문장

{% if %}
변수를 평가하여 true 이면 아래의 문장이 표시된다.
{% if athlete_list %}
	Number of athletes : {{athlete_list:length}}
{% elif athlete_in_locker_room_list %}
	Athletes should be out of the locker room soon!
{% else %}
	No athletes


{% csrf_token %}: POST 방식의 <form>을 사용하는 경우 CSRF 공격을 방지하기 위해 사용한다.
    <form action="." method="post">{% csrf_token %}

```







## 9) 기타

단축함수

```python
get_list_or_404(): 대상객체를 리스트로 가져온다. filter 함수를 사용
get_object_or_404() 대삿 get 함수를 사용
render()
```

