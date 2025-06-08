# 프로젝트 실행 가이드

## 1. Git에서 소스 다운로드
```bash
git clone https://github.com/minicens/reportPage.git
```

## 2. 프로젝트 디렉터리로 이동
```bash
cd reportPage
```

## 3. 아나콘다 환경 생성
새로운 Python 가상환경을 생성하고 활성화합니다.
```bash
conda create --name my_django_env python=3.13
conda activate my_django_env
```

## 8. 서버 실행
Django 개발 서버를 실행합니다.
```bash
python manage.py runserver
```

## 9. 브라우저에서 확인
서버가 정상적으로 실행되면 브라우저에서 아래 URL로 접속합니다.
```
http://127.0.0.1:8000/
```
