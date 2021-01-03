# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:24:10 2020

@author: 최지수
"""

##파이썬 기본 12웧 28일##
print("정보문화사-박정태")
var1=10
var2=20
print(var1)
print(var2)
var1 = var2
print(var2)
print(var1)

novar=10
print(novar)
type(var1)

print(25)
print(25.0)
print(25.1)
print(-25)
print(-25.0)

var1=25
var2=25.0
var3=25.1
var4=-25
var5=-25.0
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)


var1=25
print(var1)
var1=25.0
print(var1)


var1=10
var2=25
print(var1+var2)
print(var1-var2)
print(var1*var2)
print(var2/var1)
print(var2//var1)


##문자열 연습하기##
var1="박정태"
var2="최지수"
var2="초콜릿 먹고 싶다"
print(var2)
type(var2)

var1="hello"
var2="world"
var3=var1+" "+var2
print(var3)
var="hello world!"
print(var)
var=var.replace('!','?')
var

var=var.replace('?','')
print(var)


var='19,000원'
var=var.replace(',','').replace('원','')
print(var)


var=var.replace(',','')
print(var)
var=var.replace('원','')
print(var)

var="hello world"
finded=var.find('a')
finded2=var.find('world')
print(finded)
print(finded2)


##인덱싱이란 문자열의 특정 위치의 값을 가져오는 것!##
##슬라이싱이란 인덱싱의 확장개념으로 특정위치가 아닌 범위에 포함된 문자열을 가지고 오는 것##

var='hello world'
print(var[0])
print(var[1])
print(var[0:4])

print(var[:])
print(var[:2])
print(var[2:])

print(var[-1])
print(var[-2])
print(var[3:-2])

print(var[20])

###문자열 나누기###

var="hello world !@"
print(var.split())
print(var.split('l'))


var1="hello world"
var2="HELLO WORLD"
print(var1.upper())
print(var2.lower())

print(len(var1))


var="      hello world     "
print(var.rstrip())
print(var.lstrip())
print(var.strip())



var0=' I am' + ' 최지수'
print(var0)
var1="I am {name}".format(name="최지수")
print(var1)
var2="I am {0}".format("최지수")
print(var2)
var3="I am {0} I am {name}".format("최지수",name="파이썬 공부중")
print(var3)

var0='i am age' +25
print(var0)

age=26
var0='i am age '+ str(age)
var0
var1='i am age {0}'.format(age)
var1

var=list([1,2,3,4,5])
var=[1,2,3,4,5]
print(var)

var=[1,2,"3",4,5,6]
print(var[0])
print(var[1])
print(var[0:4])
print(var[2])

var="hello world"
print(var.split())

a=["1","2","3","4","5"]
b=".".join(a)
print(b)


a=[1,"2",3,"4","5"]
b=".".join(a)
print(b)

a=[1,2,3,4,[5,6,7]]
print(a)
print(a[4])
print(a[4][0])
print(a[4][2])
print(a[-1][0])
print(a[-1][2])


var1=[1,2,3,4,5]
var2=[6,7,8,9,10]
num=3
print(var1*3)
print(var1+var2)

var=[1,2,3,4,5]
print(var)
var[2]=10
print(var)
var[3]=[11,22,33]
print(var)

var1=[1,2,3,4,5]
var2=[1,2,3,4,5]
print(var1)
print(var1[2:4])
var1[2:4]=[0,-1]
print(var1)
var2[2:4]=[0,-1,-2]
print(var2)

var1=[1,2,3,4,5]
var1
var2=[1,2,3,4,5]
del var1[1]
print(var1)
var2[0:3]=[]
print(var2)

var=[1,2,3,4,5]
var.append(10)
print(var)
var.append(20)
print(var)



var=[1,2,3,4,5]
print(var.pop())
print(var)
var=[1,2,3,4,5,1,2,3,4,5]
print(var.remove(4))
print(var)

var=[3,5,1,2,3,4,12,13]
var.sort()
print(var)
var.sort(reverse=True)
print(var)

var=['a','d','b','c']
var.sort()
print(var)
var.sort(reverse=True)
print(var)

var=['A','d','C','b']
var.sort()
print(var)

var.sort(reverse=True)
print(var)
a=[75,"a","A",98,100]
print(a.sort())


var=[1,2,3,4,5,6,7]
len(var)

###딕셔너리##
var1=dict({"key1":"value1","key2":"value2"})
var2={"key1":"value1","key2":"vakue2"}
print(var1)
print(var2)
print(var1["key1"])
print(var2["key2"])
print(var2.get("key3"))

var={}
print(var)
var["key1"]=10
var["key2"]=20
var["key3"]=30
var["key1"]=40
print(var)

var = {}
print(var)
var.setdefault('key1',10)
var.setdefault('key1',20)
var.setdefault('key2',30)
print(var)


#key value 쌍 리스트 만들기##
var={'key1':'value1','key2':'value2','key3':'value3'}
print(var)
print(var.keys())
print(var.values())
print(var.items())

values=var.values
print(values)

var={'key1':'value1','key2':'value2','key3':'value3'}
values=var.values()
print(values)
print(values[0])
values=list(var.values())
print(values)
print(values[0])
print('key3' in var)
print('key4' in var)


##튜플##
var1=tuple((1,))
print(var1)
var



var1=(1,2,3,4,5)
print(var1[3])
print(var1[2:])

print(False and True)
print(False or True)
print(True and True)
print(1>2 or 2>1)

print(not True)
print(not 1)
print(not 0)
print(not 2)

print(not True)
print(not False)
print(not 1)
print(not 2)


condition_t=True
condition_f=False

if condition_t:
    print('hello')
    print('world')
if condition_f:
    print('HELLO')
    print('WORLD')
    
print('last')

###if else

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



if 'h' in 'hello world':
        print('hello world에 h가 포함되어 있습니다.')
if 1 in [11,22,33,44,55,66]:
        print ([11,22,33,44,55,66],'에 1이 포함됩니다.')


count=0
while count < 5:
        print('%d 번째' %(count))
        count += 1
        
        
for i in range(0,5):
    print('%d 번째' %(i))
        
for i in 'hello world':
    print(i)

for i in [11,22,33,44,55]:
    print(i)

var={'key1':'value1','key2':'value2','key3':'value3'}
for key in var:
    print(key)
    print(var[key])

print(var[key])

for i in range(2,5):
    for j in range(2,5):
        print('%d *%d = %d'% (i,j,i*j))


var ='t has sometimes been said that “behave is what organisms do. Behaviorism is built on this assumption, and its goal is to promote the scientific study of behavior. The behavior in particular, of individual organisms. Not of social groups. Not of cultures. But of persons and animals.In this entry I consider different types of behaviorism. I outline reasons for and against being a behaviorist. I consider contributions of behaviorism to the study of behavior. Special attention is given to the so-called radical behaviorism of B. F. Skinner (1904–90). Skinner is given special (not exclusive) attention because he is the behaviorist who has received the most attention from philosophers, fellow scientists and the public at large. General lessons can also be learned from Skinner about the conduct of behavioral science in general. The entry describes those lessons.'

space_ps=var.split(' ')
char_frequency ={}

for char in space_ps:
    char_frequency.setdefault(char,0)
    char_frequency[char] +=1
print(char_frequency)