# 🏥 5학년 보건수업 홈페이지

초등학교 5학년 보건 수업을 위한 학급 홈페이지입니다. 학생들은 공지사항을 확인하고 보건 선생님께 질문을 남길 수 있습니다.

## 🛠 기능

- **회원가입/로그인**: 
  - 일반 회원가입 (이름, 학번, 비밀번호)
  - **구글 계정 연동 로그인** 지원
- **게시판**:
  - 공지사항 및 질의응답 게시판 조회
  - 로그인한 사용자만 글쓰기 가능 (구현 예정)
- **관리자 기능**:
  - 서버 실행 시 관리자 계정(`abc`) 자동 생성

## 🚀 설치 및 실행 방법

### 1. 필수 요건
- Python 3.x

### 2. 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정 (.env)
프로젝트 루트에 `.env` 파일을 생성하고 보안 키를 설정할 수 있습니다 (선택 사항).
```text
SECRET_KEY=your_secret_key_here
```

### 4. 실행
```bash
python app.py
```
실행 후 브라우저에서 `http://127.0.0.1:5000`으로 접속하세요.

## 📂 기술 스택
- **Backend**: Flask, Pyrebase4
- **Frontend**: HTML5, Bootstrap 5
- **Database**: Firebase Realtime Database