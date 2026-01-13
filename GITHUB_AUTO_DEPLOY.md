# 🚀 GitHub에서 자동으로 Railway에 배포하기

## ✨ 완벽한 자동 배포 설정

이제 GitHub에 git push만 하면 **자동으로 Railway에 배포**됩니다!

---

## 📋 설정 방법 (3단계)

### Step 1: GitHub에 코드 푸시

```bash
# 배치 파일 실행 (또는 직접 git 명령)
git add .
git commit -m "Setup auto deployment to Railway"
git push origin main
```

### Step 2: Railway에 GitHub 계정 연동

1. https://railway.app 방문
2. **GitHub 계정으로 로그인** (또는 가입)
3. 우측 상단 **"+ New"** 클릭
4. **"Deploy from GitHub repo"** 선택
5. GitHub 인증 확인
6. **`lalagoola/home`** 저장소 선택

### Step 3: 환경 변수 설정 (매우 중요!)

Railway 대시보드에서:

1. **"Variables"** 탭 클릭
2. 아래 변수들을 하나씩 추가:

```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
FIREBASE_API_KEY=AIzaSyAbrKzSRUq1_Qi15yzK3aYKhOLSlhSm-2k
FIREBASE_AUTH_DOMAIN=homepage-63d32.firebaseapp.com
FIREBASE_PROJECT_ID=homepage-63d32
FIREBASE_STORAGE_BUCKET=homepage-63d32.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=515012802016
FIREBASE_APP_ID=1:515012802016:web:4c3db8588aa7f00df8a785
FIREBASE_DATABASE_URL=https://homepage-63d32-default-rtdb.firebaseio.com
PORT=8080
```

### Step 4: 배포 시작

1. Railway 대시보드에서 **"Deploy"** 또는 **"Redeploy"** 클릭
2. 잠시 대기 (약 2-3분)
3. ✅ 배포 완료!

---

## 🎯 자동 배포의 장점

```
git push origin main
       ↓
GitHub에 코드 업로드
       ↓
GitHub Actions 자동 실행
       ↓
Railway에 자동 배포
       ↓
웹사이트 업데이트 ✨
```

이제 **코드만 수정해서 git push 하면 자동으로 배포됩니다!**

---

## 🌐 배포 후 웹사이트 접속

배포 완료 후:

1. Railway 대시보드에서 "Railway.app domain" 확인
2. 예: `https://your-project-xxxxx.railway.app`
3. 클릭해서 웹사이트 방문 ✅

---

## 📊 배포 상태 확인

### Railway 대시보드에서:
- **"Deployments"** 탭 → 배포 히스토리 확인
- **"Logs"** 탭 → 실시간 로그 확인
- 에러가 있으면 로그에서 확인 가능

### GitHub에서:
- **"Actions"** 탭 → 자동 배포 워크플로우 상태 확인

---

## 🔄 코드 수정 후 자동 배포

```bash
# 파일 수정
# 예: templates/index.html 변경

# 변경사항 git으로 커밋
git add .
git commit -m "Update homepage design"
git push origin main

# 자동으로 Railway에 배포됨! 🚀
```

1-2분 후 웹사이트에서 변경사항 확인 가능!

---

## 🚨 환경 변수가 누락되면?

배포 후 로그에 오류:
```
ModuleNotFoundError: No module named 'firebase'
또는
Error: FIREBASE_API_KEY is not defined
```

해결:
1. Railway 대시보드로 이동
2. **"Variables"** 탭 확인
3. 모든 FIREBASE_* 변수가 있는지 확인
4. 누락된 것 추가
5. **"Redeploy"** 클릭

---

## 💡 팁

### 1. 커스텀 도메인 설정 (선택사항)
1. Railway 대시보드 → "Settings"
2. "Railway.app domain" 또는 커스텀 도메인 설정 가능

### 2. 무료 크레딧 확인
- Railway는 월 5달러 무료 크레딧 제공
- 일반적인 Flask 앱은 충분함

### 3. 배포 실패 시
1. 로그 확인: Logs 탭
2. 환경 변수 재확인
3. requirements.txt 확인 (필요한 패키지 모두 있는지)
4. GitHub Actions 로그도 확인

---

## 🎉 축하합니다!

이제 진정한 자동 배포 시스템이 완성되었습니다!

```
GitHub (코드 저장소) ← git push
       ↓ 자동
Railway (배포 서버) ← 자동 배포
       ↓
https://your-app.railway.app (사용자 방문)
```

---

## 📚 다음 링크

- [Railway 공식 문서](https://docs.railway.app)
- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [Flask 배포 가이드](https://flask.palletsprojects.com/en/latest/deploying/)

**이제 완벽한 배포 파이프라인을 갖췄습니다!** 🚀
