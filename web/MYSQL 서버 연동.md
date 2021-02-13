# MYSQL 서버 연동

### mysql 연동/접속방법

#### root로 로그인

```
mysql - u root -p
```

#### yyhj 계정 생성

```
create user 'yyhj'@'localhost' identified by 'yy1234';
```

#### 데이터베이스 생성

```
create database nsgdb character set utf8;
```

#### yyhj에 권한 모두 부여

```
grant all on nsgdb.* to 'yyhj'@'localhost';
flush privileges;
```

#### makemigrations

```
python manage.py makemigrations
```

#### migrate

```
python manage.py migrate
```

#### 접속확인

```
mysql -u root -p
use nsgdb;
show tables;
```

### 도움이 될만한 mysql 명령어들

```
use DB이름 # 명시한 데이터베이스를 사용
show tables; # 현재 사용중인 db 내의 테이블 목록을 보여줍니다
show databases; # 전체 데이터베이스의 목록을 보여줍니다
mysql -u root -p 비밀번호
use mysql; # 계정 정보 등을 담고 있는 mysql 기본 db 입니다
select host, user from user; # user 테이블(계정 정보를 담고 있는 테이블)에서 host와 user(이름)에 대한 정보를 조회
```



**mysql 연동 순서 (projectnsg 기준)**

1. mysql 다운 후, root 설정
2. 프롬프트에서 root 로그인
3. create user '사용자'@'localhost' identified by '비밀번호';   (# 사용자: yyhj, 비밀번호: yy1234)
4. show databases; 로 현재 DB 확인
5. create database nsgdb character set utf8;  (#db 생성)
6. show databeses; 로 **'추가된'** DB 확인
7. grant all on nsgdb.* to 'yyhj'@'localhost';  (# nsgdb.*: 추가된 DB)
8. flush privileges; (# grant 테이블을 reload함으로서 변경 사항을 즉시 반영)
9. mysql exit
10. 프롬프트에서 프로젝트 파일로 이동 후 python manage.py makemigrations
11. 이후 python manage.py migrate
12. mysql -u root -p로 로그인 후 use nsgdb;
13. show tables; 로 테이블 확인