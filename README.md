# 🏥 5학년 보건수업 홈페이지

> 초등학교 5학년 학생 및 학부모를 위한 **친화적이고 예쁜 보건 수업 홈페이지**

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Flask 2.3](https://img.shields.io/badge/Flask-2.3-green)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ 주요 특징

### 👨‍👩‍👧‍👦 사용자 친화적 디자인
- 🎨 **밝고 예쁜 컬러** - 5학년 학생들이 좋아하는 오렌지, 파랑, 보라색 조화
- 📱 **반응형 디자인** - 모든 기기에서 완벽하게 표시
- ✨ **부드러운 애니메이션** - 인터랙티브한 사용자 경험
- 🎉 **재미있는 이모지** - 친근하고 즐거운 느낌

### 🔐 안전한 계정 관리
- 📝 **회원가입** - 이름, 학년 반 번호, 비밀번호로 가입
- 🔐 **로그인** - 안전한 세션 기반 로그인
- 🔑 **구글 로그인** - Firebase 인증으로 간편한 구글 계정 연동
- ✅ **입력 검증** - 모든 입력값에 대한 검증

### 📢 정보 공유
- **공지사항** - 보건 선생님의 중요한 소식 공유
- **질의응답** - 학생들의 건강 관련 질문과 답변
- **보안된 세션** - 로그인한 사용자 정보 안전 보관

## 🛠 기술 스택

| 분류 | 기술 |
|------|------|
| **Backend** | Flask 2.3 |
| **Database** | Firebase Realtime Database |
| **Authentication** | Firebase Authentication (구글 로그인) |
| **Frontend** | HTML5, Bootstrap 5, JavaScript |
| **Fonts** | Noto Sans KR, Jua (구글 폰트) |

## 📋 설치 및 실행

### 1. 필수 사항
- Python 3.7 이상

### 2. 저장소 복제
```bash
git clone https://github.com/yourusername/health-class-homepage.git
cd health-class-homepage
```

### 3. 가상 환경 생성 (권장)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. 의존성 설치
```bash
pip install -r requirements.txt
```

### 5. 환경 변수 설정
프로젝트 루트에 `.env` 파일을 생성합니다:
```text
SECRET_KEY=your_secret_key_here
```

### 6. 애플리케이션 실행
```bash
python app.py
```

브라우저에서 `http://localhost:5000` 으로 접속하세요! 🎉

## 📁 프로젝트 구조

```
health-class-homepage/
├── app.py                      # Flask 메인 애플리케이션
├── requirements.txt            # Python 패키지 의존성
├── .env                        # 환경 변수 (git에 추가하지 마세요)
├── .gitignore                  # Git 제외 파일 목록
├── README.md                   # 프로젝트 설명서
├── LICENSE                     # MIT 라이선스
├── templates/                  # HTML 템플릿
│   ├── base.html               # 기본 레이아웃
│   ├── index.html              # 홈 페이지
│   ├── login.html              # 로그인 페이지
│   ├── signup.html             # 회원가입 페이지
│   └── board.html              # 게시판 페이지
└── static/                     # 정적 파일
    ├── css/                    # CSS 파일
    └── js/                     # JavaScript 파일
```

## 🔑 주요 기능 설명

### 🏠 홈페이지 (`/`)
- 보건수업 홈페이지 안내
- 공지사항 및 질의응답 링크
- 미로그인 사용자용 회원가입/로그인 유도

### 📝 회원가입 (`/signup`)
- 이름, 학년 반 번호, 비밀번호 입력
- 중복 아이디 확인
- 구글 계정 연동 가입 옵션

### 🔐 로그인 (`/login`)
- 아이디(이름)와 비밀번호로 로그인
- 구글 계정 로그인 옵션
- 에러 메시지 표시

### 📢 게시판 (`/board/<type>`)
- **공지사항** (`/board/notice`) - 보건 선생님의 공지사항
- **질의응답** (`/board/qna`) - 학생들의 질문과 답변

### 🚪 로그아웃 (`/logout`)
- 현재 세션 종료

## 👥 사용자 가이드

### 학생들을 위해
1. **회원가입**: 이름과 학년 반 번호를 입력하고 가입합니다
2. **로그인**: 아이디와 비밀번호로 로그인합니다
3. **공지사항 확인**: 보건 선생님의 중요한 소식을 확인합니다
4. **질문하기**: 궁금한 점을 질의응답 게시판에 남깁니다

### 학부모들을 위해
- 자녀의 건강 정보와 학교 공지사항을 한곳에서 확인할 수 있습니다
- 구글 계정으로 간편하게 로그인 가능합니다

## 🔒 보안 사항

- 비밀번호는 Firebase에 저장되며, 최소 4자 이상이어야 합니다
- 세션 기반 인증으로 사용자 정보 보호
- 구글 로그인은 Firebase OAuth 2.0을 사용합니다
- `.env` 파일에는 민감한 정보가 포함되므로 **git에 추가하지 마세요**

## 📝 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)를 따릅니다.

## 🤝 기여 가이드

1. Fork 한 후 기능 브랜치를 생성합니다 (`git checkout -b feature/AmazingFeature`)
2. 변경사항을 커밋합니다 (`git commit -m 'Add some AmazingFeature'`)
3. 브랜치에 Push 합니다 (`git push origin feature/AmazingFeature`)
4. Pull Request를 생성합니다

## 📧 문의 및 피드백

문제가 생기거나 개선 사항이 있으시면 [이슈](https://github.com/yourusername/health-class-homepage/issues)를 등록해주세요.

## 🎓 학습 자료

이 프로젝트는 다음 기술들을 학습하는 데 도움이 됩니다:
- Flask 웹 프레임워크
- Firebase 데이터베이스 및 인증
- HTML/CSS/JavaScript
- Bootstrap 프레임워크
- 반응형 웹 디자인

## 🌟 개발 로드맵

- [ ] 게시글 작성 기능
- [ ] 파일 업로드 기능
- [ ] 댓글 기능
- [ ] 공지사항 카테고리 분류
- [ ] 검색 기능
- [ ] 사용자 프로필 페이지
- [ ] 알림 기능

---

**만든이**: [Your Name]  
**마지막 업데이트**: 2024년 1월