# 1. MySQL

* Database Management System 
  * database와 다르다. database를 관리하는 시스템이다. 

![KakaoTalk_20210113_162554849](md-images/KakaoTalk_20210113_162554849.png)

1. MySQL 5.6버전을 받으러 가요!
2. 다운로드 후 바탕화면에 복사해요. 그리고 압축을 풀어요
3. bin폴더로 들어가서 다음의 명령을 도스창에서 실행해요!
4. 도스창에서 => msqld    (mysql DBMS를 기동시키는 명령어)
5. 만약 정상적으로 시작되면 mysql daemon이 동작하게 되요!
6. 데이터베이스를 정상적으로 종료하려면 새로운 도스창을 띄워요!
   mysqladmin -u root shutdown
7. 서버를 기동한 상태에서
8. 데이터베이스는 사용자 ID/PW가 있어야지 사용할 수 있어요!
   그래서 새로운 사용자의 ID와 PW를 설정해 줄꺼예요!
   그러기 위해서 먼저 mysql console에 들어갈꺼예요!(관리자 권한으로)
   mysql -u root
9. console에 들어가면 mysql> 프롬프트가 보여요!!
10. 정상적으로 접속했으면 새로운 사용자를 다음의 명령어를 이용해서 만들어요
    create user data identified by "data";
11. 외부접속을 위해 다음의 명령을 한번 더 실행합니다.
    create user data@localhost identified by "data";
12. 데이터가 저장될 데이터베이스를 생성해야 해요!!
    우리가 사용하는 mysql은 DBMS(Database Management System)
    여러개의 Database를 관리하는 프로그램이예요!
    create database library;
13. 새로운 사용자(data)가 새로만든 데이터베이스(library)를 사용할 수 있도록
    권한을 부여할꺼예요!
    grant all privileges on library.* to data;
    grant all privileges on library.* to data@localhost;

![KakaoTalk_20210113_163227790](md-images/KakaoTalk_20210113_163227790.png)

14. 권한 설정에 대한 refresh를 시켜줘요!
    flush privileges;
15. 설정은 다 끝났으니 이제 console에서 나와요!! 
    exit;
    도스창에서 제공된 script file을 이용해서 데이터를 적재할 꺼예요!
    mysql -u data -p library < _BookTableDump.sql

![KakaoTalk_20210113_164553730](md-images/KakaoTalk_20210113_164553730-1610543464129.png)