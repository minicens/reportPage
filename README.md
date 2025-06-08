# 프로젝트 실행 가이드

## 1. Git에서 소스 다운로드
```bash
git clone https://github.com/minicens/reportPage.git
```

## 2. 프로젝트 디렉터리로 이동
```bash
cd reportPage
```

## 3. 아나콘다 설치 및 활성화
```bash
conda create -n ll_env python=3.12
conda activate ll_env
```
## 4. 장고 설치
```bash
conda install django
```

## 5. 장고서버 실행
Django 개발 서버를 실행합니다.
```bash
python manage.py runserver
```

## 6. 브라우저에서 확인
```
http://127.0.0.1:8000/
```
